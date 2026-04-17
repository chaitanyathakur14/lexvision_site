import cv2
import numpy as np
import pytesseract

def process_document(image_path):
    img = cv2.imread(image_path)
    # FR-01: Pre-processing (Module 3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Bilateral Filter for noise removal while keeping text edges sharp
    denoised = cv2.bilateralFilter(gray, 9, 75, 75)
    # Otsu Binarization
    _, thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # FR-04: OCR Extraction (Module 5)
    text_data = pytesseract.image_to_string(thresh)
    # FR-03: Stamp/Signature Detection (Module 4/5)
    # Simple Blob detection for signatures
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    signature_found = any(cv2.contourArea(c) > 500 for c in contours) # Threshold area

    return {
        "text": text_data,
        "verified": signature_found,
        "processed_image": thresh
    }