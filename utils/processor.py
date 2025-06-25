from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import torch

# Load tokenizer and model once
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def get_bert_embedding(text):
    """Generate a BERT [CLS] token embedding for a given text."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    inputs = {key: val.to(device) for key, val in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the [CLS] token embedding
    return outputs.last_hidden_state[:, 0, :].cpu().numpy().flatten()

def compute_similarity(jd_text, resumes_texts):
    """
    Compare JD with each resume and return a sorted list of (resume_name, similarity_score)
    """
    jd_vector = get_bert_embedding(jd_text)
    result = []

    for name, resume_text in resumes_texts:
        resume_vector = get_bert_embedding(resume_text)
        score = cosine_similarity([jd_vector], [resume_vector])[0][0]
        result.append((name, score))

    return sorted(result, key=lambda x: x[1], reverse=True)
