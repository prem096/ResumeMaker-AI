from extensions import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class MatchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    mode = db.Column(db.String(20))  # "recruiter" or "candidate"
    file1 = db.Column(db.String(120))  # Resume or JD
    file2 = db.Column(db.String(120))  # JD or Resume
    score = db.Column(db.Float)
    matched_skills = db.Column(db.Text)
    missing_skills = db.Column(db.Text)
    extra_skills = db.Column(db.Text)
    inferred_role = db.Column(db.String(50))
    summary_file = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
