import csv
import os
from datetime import datetime

HISTORY_FILE = "user_data/history.csv"
os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

def save_history(user_id, mode, resume_name, jd_name, score, matched, missing, extra, inferred_role, summary_file):
    """
    Save a match entry into the history CSV file.
    """
    with open(HISTORY_FILE, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            user_id,
            mode,
            resume_name,
            jd_name,
            round(score * 100, 2),
            ", ".join(matched),
            ", ".join(missing),
            ", ".join(extra),
            inferred_role,
            summary_file,
            datetime.now().isoformat()
        ])

def load_user_history(user_id):
    """
    Load all history entries for the given user.
    """
    if not os.path.exists(HISTORY_FILE):
        return []
    
    history = []
    with open(HISTORY_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == str(user_id):
                history.append({
                    "mode": row[1],
                    "file1": row[2],     # Resume or JD
                    "file2": row[3],     # JD or Resume
                    "score": float(row[4]),
                    "matched": row[5].split(", ") if row[5] else [],
                    "missing": row[6].split(", ") if row[6] else [],
                    "extra": row[7].split(", ") if row[7] else [],
                    "inferred_role": row[8],
                    "summary_file": row[9],
                    "timestamp": datetime.fromisoformat(row[10])
                })
    return history
