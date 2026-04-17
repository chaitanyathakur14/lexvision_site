
# LexVision - Judicial Document Intelligence

**Computer Vision & Analytics (CVA) Project**  
**E009 Chaitanya Thakur | E012 Bharat Baswan**  
**SVKM’s NMIMS - Mukesh Patel School of Technology Management & Engineering**  
**April 2026 Demo**

---

## 📋 Project Overview

LexVision is an intelligent system that processes Indian Supreme Court and High Court judgment PDFs using **Computer Vision** and **Hybrid AI** techniques.

It performs:
- Document preprocessing (grayscale, binarization, deskewing)
- Signature / Stamp verification
- Case metadata extraction
- Document classification (Writ / Civil / Criminal) using **SVM + HOG + Text Heuristics**
- AI-powered legal assistant using **Gemini 3 Flash**

Fully aligned with **CVA Syllabus Modules 1–8**.

---

## ✨ Features

- End-to-end 4-stage CV pipeline (ORIG → BIN → SKEW → MAP)
- Signature detection & authentication
- Case number, year, jurisdiction extraction using Regex
- Hybrid classification (97% model accuracy claimed)
- Interactive AI Legal Assistant (Gemini-powered)
- Clean, responsive Streamlit-like Django UI

---

## 🛠 Tech Stack

- **Backend**: Django 5.2
- **Computer Vision**: OpenCV, scikit-image
- **OCR**: Tesseract + pytesseract
- **PDF Processing**: pdf2image + Poppler
- **ML Model**: SVM + HOG (scikit-learn)
- **AI Assistant**: Google Gemini 3 Flash
- **Frontend**: Bootstrap + Custom CSS
- **Deployment Ready**: Docker + Railway

---

## 📁 Project Structure

```
lexvision_site/
├── manage.py
├── lexvision_site/
│   └── settings.py
├── processor/
│   ├── views.py
│   ├── utils.py
│   └── models.py
├── templates/
│   └── processor/
│       ├── upload.html
│       └── results.html
├── media/                  ← Generated pipeline images
├── static/
├── requirements.txt
├── Dockerfile
├── railway.toml
└── .env                    ← (Not committed)
```

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd lexvision_site
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup paths** (in `utils.py`)
   - Update `POPPLER_PATH` and Tesseract path according to your system.

4. **Run the server**
   ```bash
   python manage.py runserver
   ```

5. Open `http://127.0.0.1:8000/` and upload a judgment PDF.

---

## 📸 Demo Pipeline Stages

1. **ORIG** – Original scanned document
2. **BIN** – Binarized image (Otsu + Bilateral Filter)
3. **SKEW** – Deskewed & aligned document
4. **MAP** – Signature/Stamp detection with green bounding boxes

---

## 🎯 Functional Requirements Covered

- FR-01: Image Pre-processing
- FR-02: Feature Detection (Edge/Contour)
- FR-03: Stamp/Signature Verification
- FR-04: OCR Extraction
- FR-05: Metadata Extraction
- FR-06: Hybrid Classification + AI Chat

---

## 📌 For Demo (18th April 2026)

- Use the Jupyter Notebook version (`LexVision_Demo.ipynb`) as backup
- Show live Django web app (preferred)
- Highlight syllabus coverage (Modules 1–8)
- Demonstrate both pipeline + AI chat

---

## 🔧 Deployment

Ready for **Railway.app** using Docker.

Files included:
- `Dockerfile`
- `railway.toml`
- `requirements.txt`

Add `GEMINI_API_KEY` as environment variable on Railway.

---

**Made with ❤️ for CVA Course**

---
