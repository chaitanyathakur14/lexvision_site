# Legal Document Summarization Pipeline for Indian Supreme Court Judgments


---

## Overview

Developed a complete research-grade pipeline for **extractive and abstractive summarization** of long legal documents. Processed **1,999 Supreme Court of India judgments** (2020–2024) and conducted a rigorous comparative evaluation of four models: **TF-IDF, TextRank, BART, and T5**.

The pipeline includes robust PDF ingestion with OCR fallback, intelligent chunking for very long documents, multiple summarization approaches, and comprehensive evaluation using ROUGE, BERTScore, and Wilcoxon statistical significance tests.

This work highlights important differences between lexical overlap (ROUGE) and semantic similarity (BERTScore) in the **legal domain**.

---

## Key Features

- Robust 3-layer PDF text extraction (pdfplumber → PyMuPDF → Tesseract OCR + OpenCV preprocessing)
- Sliding window chunking with overlap for long judgments (up to 136k words)
- Extractive Summarization: TF-IDF + TextRank
- Abstractive Summarization: BART-large-cnn + T5-small
- Headnote-based automatic reference summary extraction
- Year-stratified train/val/test split (70/15/15)
- Multi-metric evaluation + statistical significance testing (Wilcoxon)
- Reproducible results with saved CSVs and visualizations

---

## Dataset Statistics

- **Total Documents:** 1,999
- **Average Length:** 9,873 words
- **Median Length:** 6,028 words
- **Year Distribution:** ~400 judgments per year (2020–2024)
- **Splits:** Train (1,399), Val (300), Test (300)

---

## Results Summary

| Model     | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore-F1 | Avg Time (s) | Coverage |
|-----------|---------|---------|---------|--------------|--------------|----------|
| **TF-IDF**    | **0.4927** | **0.3937** | **0.3106** | **0.8272** | **0.01** | 300/300 |
| TextRank  | 0.4405  | 0.3478  | 0.2932  | 0.8227       | 0.02         | 300/300 |
| BART      | 0.2898  | 0.1941  | 0.2305  | 0.8231       | 28.56        | 288/300 |
| T5        | 0.2787  | 0.1919  | 0.2179  | 0.8020       | 11.89        | 300/300 |

**Key Insight:** TF-IDF performs best on ROUGE metrics, while BART achieves near-parity on semantic quality (BERTScore) despite lower lexical overlap.  
Wilcoxon Signed-Rank tests confirm extractive methods are **statistically significantly better** than abstractive ones on ROUGE metrics (p < 0.001).

---

## Tech Stack

- **Core:** Python, Pandas, NumPy, scikit-learn, NetworkX
- **NLP:** Hugging Face Transformers (BART, T5), ROUGE, BERTScore
- **PDF/OCR:** pdfplumber, PyMuPDF, Tesseract, OpenCV
- **Visualization:** Matplotlib, Seaborn

---

---

## Project Demo Data Preprocessing - Final images of entire deployment will be updated soon!
End-to-End Pipeline
![LexVision Pipeline Analysis](lex_1.png)
![LexVision Pipeline Analysis](lex_2.png)
![LexVision Pipeline Analysis](lex_3.png)
### Legal Assistant Chat
![LexVision Assistant](lex_4.png)

## How to Run

```bash
git clone <your-repo-url>
cd legal-document-summarization

pip install -r requirements.txt
python pipeline.py

##Project Demo Data Preprocessing
End-to-End Pipeline
![LexVision Pipeline Analysis](lex_1.png)
![LexVision Pipeline Analysis](lex_2.png)
![LexVision Pipeline Analysis](lex_3.png)
### Legal Assistant Chat
![LexVision Assistant](lex_4.png)


## Project Structure
