# LexVision - Judicial Document Intelligence

**Computer Vision & Analytics (CVA) Project**  
**E009 Chaitanya Thakur | E012 Bharat Baswan**  
**SVKM’s NMIMS - Mukesh Patel School of Technology Management & Engineering**  
**April 2026 Demo**

---

## Project Overview

LexVision is an intelligent system that processes Indian Supreme Court and High Court judgment PDFs using **Computer Vision** and **Hybrid AI** techniques.

It performs:
- Document preprocessing (grayscale, binarization, deskewing)
- Signature / Stamp verification
- Case metadata extraction
- Document classification (Writ / Civil / Criminal) using **SVM + HOG + Text Heuristics**
- AI-powered legal assistant using **Gemini 3 Flash**

Fully aligned with **CVA Syllabus Modules 1–8**.

---

## Features

- End-to-end 4-stage CV pipeline (ORIG → BIN → SKEW → MAP)
- Signature detection & authentication
- Case number, year, jurisdiction extraction using Regex
- Hybrid classification (97% model accuracy claimed)
- Interactive AI Legal Assistant (Gemini-powered)
- Clean, responsive Streamlit-like Django UI

---

## Tech Stack

- **Backend**: Django 5.2
- **Computer Vision**: OpenCV, scikit-image
- **OCR**: Tesseract + pytesseract
- **PDF Processing**: pdf2image + Poppler
- **ML Model**: SVM + HOG (scikit-learn)
- **AI Assistant**: Google Gemini 3 Flash
- **Frontend**: Bootstrap + Custom CSS
- **Deployment Ready**: Docker + Railway

---

##  Project Structure
