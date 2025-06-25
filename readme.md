# 📄 ResumeRanker AI

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![Chart.js](https://img.shields.io/badge/Chart.js-4.x-blueviolet)
![Status](https://img.shields.io/badge/Project-Ready--to--Deploy-green)

ResumeRanker AI is a smart resume screening tool that analyzes how well candidate resumes match a given job description using NLP techniques. It visualizes scores using a bar chart and provides results in tabular and downloadable CSV formats.

---

## 🚀 Features

- 🔍 Upload a Job Description and multiple resumes (PDFs)
- 🧠 Compute similarity using TF-IDF (or BERT upgrade ready)
- 📊 Visualize results using Chart.js
- 🧾 Export matching scores as downloadable CSV
- 📱 Responsive Bootstrap UI
- 🧼 Clean and professional UI with success/error handling

---

## 📸 Screenshot

<table>
<tr>
<td><img src="https://user-images.githubusercontent.com/your-image-link/chart-demo.png" width="450"/></td>
<td><img src="https://user-images.githubusercontent.com/your-image-link/table-demo.png" width="450"/></td>
</tr>
</table>

---

## 🛠️ Tech Stack

- Python 3.9+
- Flask
- scikit-learn
- fitz (PyMuPDF)
- Chart.js
- Bootstrap 5

---

## 🧪 How It Works

1. Upload a **Job Description** (JD) PDF
2. Upload multiple **Resume** PDFs
3. System extracts raw text using PyMuPDF
4. Uses TF-IDF to compare each resume to the JD
5. Scores are shown in a table and bar chart
6. Results can be downloaded as a CSV file

---

## 📂 Project Structure

