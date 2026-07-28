# Legal Document Summarization Pipeline for Indian Supreme Court Judgments

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)]()

A research-grade pipeline for **extractive and abstractive summarization** of long legal documents, benchmarking **TF-IDF, TextRank, BART, and T5** on **1,999 Supreme Court of India judgments** (2020–2024).

---

## Key Finding

TF-IDF wins on ROUGE, but that's not the whole story:

- **ROUGE says extractive wins.** TF-IDF leads all models on ROUGE-1/2/L (statistically significant, Wilcoxon p < 0.001 vs. every other model).
- **BERTScore tells a different story.** BART (0.8231) nearly matches TF-IDF (0.8272) on semantic similarity despite scoring far lower on ROUGE-L (0.2305 vs. 0.3106).
- **Human raters invert the ROUGE ranking entirely.** Across 20 blind-rated test documents, T5 and BART score highest on readability, legal correctness, and factual preservation — while TF-IDF (the top ROUGE performer) scores *lowest* on readability (2.62/5).

This gap exists because the reference summaries (headnote excerpts) are themselves extractive, which structurally rewards extractive methods on lexical-overlap metrics. The practical takeaway: **don't trust ROUGE alone to judge abstractive legal summarization** — pair it with BERTScore and human review.

---

## Pipeline Overview

1. **PDF Ingestion (3-layer fallback):** pdfplumber → PyMuPDF → Tesseract OCR (with OpenCV grayscale/Otsu/CLAHE/deskew preprocessing). On a 200-doc sample, Layer 1 handled 100% of documents; OCR reliability was independently validated at 94.6% character accuracy / 87.6% word accuracy on forced-OCR tests.
2. **Classification & Authentication:** Rule-based keyword classifier (Criminal/Civil/Constitutional/Service) — 97% overall accuracy (macro-F1 0.74, weighted F1 0.95) against 60 manually labelled documents. Struggles specifically on the small Constitutional class (F1 = 0.00, n = 2).
3. **Chunking:** Sliding-window chunker (3,000 chars, 200 overlap) for judgments up to 136,343 words, with hierarchical second-pass summarization for long merged outputs.
4. **Summarization:**
   - Extractive: TF-IDF sentence scoring, TextRank (PageRank over TF-IDF cosine-similarity graph)
   - Abstractive: BART (facebook/bart-large-cnn), T5 (t5-small), both chunk-then-summarize
5. **Reference Summaries:** Headnote heuristic (text before "JUDGMENT", bounded to 150–400 words).
6. **Evaluation:** ROUGE-1/2/L, batched BERTScore (roberta-base), inference timing, Wilcoxon signed-rank significance testing, and a blind 3-rater human evaluation (98 rated summaries across 20 documents stratified by length).

---

## Results

### Automatic Metrics (n = 300 test documents, except BART n = 288*)

| Model    | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore-F1 | Avg Time (s) |
|----------|---------|---------|---------|--------------|--------------|
| **TF-IDF**   | **0.4927** | **0.3937** | **0.3106** | 0.8272 | 0.01 |
| TextRank | 0.4405  | 0.3478  | 0.2932  | 0.8227 | 0.02 |
| BART     | 0.2898  | 0.1941  | 0.2305  | **0.8231** | 28.56 |
| T5       | 0.2787  | 0.1919  | 0.2179  | 0.8020 | 11.89 |

\* BART could not generate summaries for 12/300 test documents due to tokenizer/indexing errors on short chunk boundaries; these were excluded from BART's scoring only.

### Human Evaluation (mean of 3 blind raters, 1–5 scale, n = 18–20 per model)

| Model    | Readability | Legal Correctness | Factual Preservation |
|----------|-------------|--------------------|-----------------------|
| TF-IDF   | 2.62        | 3.75               | 4.05 |
| TextRank | 3.97        | 4.03               | 4.00 |
| BART     | **4.11**    | **4.11**           | 4.22 |
| T5       | 4.02        | 4.18               | **4.37** |

Inter-rater reliability: Pearson r = 0.73 (readability), 0.58 (legal correctness), 0.60 (factual preservation); within-1 agreement ≥ 93%.

### Statistical Significance

Wilcoxon signed-rank tests on ROUGE-1 confirm every extractive-vs-abstractive pair is significant (p < 0.001). BART vs. T5 shows no significant difference (p = 0.133).

---

## Repository Contents

```
dataset/splits/train.csv           # 1,399 documents (70%)
dataset/splits/val.csv             # 300 documents (15%)
dataset/splits/test.csv            # 300 documents (15%)
assets/results_raw.csv             # all model summaries + timings
assets/final_metrics.csv           # ROUGE + BERTScore table
assets/dataset_stats.csv           # corpus statistics
assets/wilcoxon_significance.csv   # pairwise significance tests
assets/error_analysis_worst_cases.csv  # 5 worst BART/T5 cases w/ diagnostics
assets/sample_output_table.csv     # side-by-side qualitative comparison
assets/computational_environment.csv
```

---

## Tech Stack

- **Core:** Python 3.12, Pandas, NumPy, scikit-learn, NetworkX
- **NLP:** Hugging Face Transformers (BART, T5), rouge-score, bert-score
- **PDF/OCR:** pdfplumber, PyMuPDF, Tesseract, OpenCV
- **Stats:** SciPy (Wilcoxon signed-rank)
- **Visualization:** Matplotlib, Seaborn

---

## Setup & Usage

```bash
git clone <your-repo-url>
cd legal-document-summarization

pip install -r requirements.txt
# or manually:
pip install pdfplumber pymupdf pytesseract pillow opencv-python-headless
pip install transformers torch torchvision
pip install rouge_score bert_score
pip install sumy nltk scikit-learn pandas numpy tqdm

python pipeline.py
```

**Requirements:** Tesseract OCR installed system-side for the OCR fallback layer. Runs CPU-only by default; a CUDA GPU will substantially speed up BART/T5 inference (28.56s and 11.89s/doc on CPU respectively).

---

## Limitations

- Reference summaries are heuristically extracted headnotes, not human-written abstracts — this structurally favors extractive methods on ROUGE.
- BART/T5 are used pretrained, general-domain, with no fine-tuning on Indian legal text.
- Input is truncated to 600 words before summarization, which can drop later sections (operative orders, final dispositions) of long judgments.
- BART fails on 4% of test documents (tokenizer/indexing limits).
- Rule-based classifier is unreliable on the small Constitutional category (F1 = 0.00, n = 2).
- Human evaluation covers only 20/300 test documents (6.7%).

## Future Work

- Fine-tune domain-adapted models (Legal-Pegasus, LegalBERT-based encoder-decoders, Longformer Encoder-Decoder for up to 16K tokens) on Indian legal corpora.
- Extend human evaluation to a larger panel across the full test set.
- Multilingual extension to regional Indian languages.

---

## Dataset Source

Corpus sourced via a [Kaggle-hosted dataset](https://www.kaggle.com/datasets/adarshsingh0903/legal-dataset-sc-judgments-india-19502024), originally compiled from the Supreme Court of India's official digital repository and Indian Kanoon.
