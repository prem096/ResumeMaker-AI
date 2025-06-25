# 🤖 ResumeRanker AI

> An AI-powered web application to match resumes with job descriptions and rank them based on skill alignment and role inference.

ResumeRanker AI helps **recruiters** find the most suitable candidates from a batch of resumes, and allows **candidates** to evaluate their resumes against multiple job descriptions. It uses **Natural Language Processing (NLP)** and **Transformer-based models (BERT)** to compute similarity and extract skill relevance.

---

## 🚀 Features

- 🔍 **Dual Modes**:  
  - **Recruiter Mode**: Upload a JD and multiple resumes → Get ranked candidates  
  - **Candidate Mode**: Upload your resume and multiple JDs → Get ranked jobs

- 🧠 **AI/NLP Matching**:  
  Uses BERT embeddings and SpaCy to match content meaningfully, not just by keywords.

- 📊 **Skill Analysis**:  
  Extracts **matched**, **missing**, and **extra skills** using a custom skill dictionary.

- 📁 **PDF Summary Reports**:  
  Generate detailed downloadable summaries with charts for each comparison.

- 📈 **Interactive Dashboard**:  
  Filter results by role, score, or skills; visualize match scores using charts.

- 🧾 **User Authentication**:  
  Login and register securely using Flask-Login and SQLite.

- 💾 **Match History Tracking**:  
  Each user's comparisons are saved for future review.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, Bootstrap 5
- **Backend**: Flask (Python)
- **AI Models**: BERT (from HuggingFace Transformers), SpaCy
- **Database**: SQLite + SQLAlchemy
- **PDF Generation**: WeasyPrint + Matplotlib
- **Authentication**: Flask-Login

---

## 🔧 Installation

### 1. Clone the repo
```bash
git clone https://github.com/your-username/resumeranker-ai.git
cd resumeranker-ai
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
