import spacy
from spacy.pipeline import EntityRuler
import json
import os

# Load SpaCy model safely
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise RuntimeError("Run `python -m spacy download en_core_web_sm` to install the model.")

# Load skills.json: a dictionary of {canonical_skill: [synonyms]}
def load_skills(filepath="utils/skills.json"):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Skill file not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Dynamically add skill patterns to SpaCy pipeline
def add_skill_ruler(nlp, skill_dict):
    if "entity_ruler" in nlp.pipe_names:
        nlp.remove_pipe("entity_ruler")
    ruler = nlp.add_pipe("entity_ruler", before="ner", config={"overwrite_ents": True})

    patterns = []
    for canonical, synonyms in skill_dict.items():
        for phrase in synonyms:
            patterns.append({"label": "SKILL", "pattern": phrase})
    ruler.add_patterns(patterns)

# Fallback chunks: for text that didn't match any patterns
def extract_candidate_chunks(doc):
    return [chunk.text.strip().lower() for chunk in doc.noun_chunks if len(chunk.text.strip()) > 2]

# Main skill extractor
def extract_skills(text, skill_dict, use_fallback_chunks=True):
    add_skill_ruler(nlp, skill_dict)
    doc = nlp(text)
    detected = set()

    # Extract entities labeled as SKILL
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            detected.add(ent.text.strip().lower())

    # Optional fallback using noun chunks
    if use_fallback_chunks:
        known_phrases = {phrase.lower() for synonyms in skill_dict.values() for phrase in synonyms}
        for chunk in extract_candidate_chunks(doc):
            if chunk in known_phrases:
                detected.add(chunk)

    return sorted(detected)

# Skill overlap comparison
def compare_skills(jd_text, resume_text, skill_dict):
    jd_skills = set(extract_skills(jd_text, skill_dict))
    resume_skills = set(extract_skills(resume_text, skill_dict))

    matched = sorted(resume_skills & jd_skills)
    missing = sorted(jd_skills - resume_skills)
    extra = sorted(resume_skills - jd_skills)
    return matched, missing, extra

# Suggestions based on missing skills
def generate_suggestions(missing_skills, descriptions=None):
    suggestions = []
    descriptions = descriptions or {}
    for skill in missing_skills:
        line = f"Consider learning {skill}"
        if skill in descriptions:
            line += f" ({descriptions[skill]})"
        suggestions.append(line)
    return suggestions

# Infer most likely role based on skill overlap
def infer_job_role(resume_skills, role_skill_map):
    scores = {
        role: len(set(resume_skills) & set(skills))
        for role, skills in role_skill_map.items()
    }
    return max(scores, key=scores.get) if scores else "Unknown"
