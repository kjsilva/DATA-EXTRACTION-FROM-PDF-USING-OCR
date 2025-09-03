# 📄 DATA-EXTRACTION-FROM-PDF-USING-OCR

## 📌 Project Overview
This project automates **data extraction from PDF files** using **OCR (Optical Character Recognition)** techniques.  
The pipeline uses:

- **[PyMuPDF (fitz)]** → to render PDF pages into images.  
- **[OpenCV]** → for image preprocessing (deskewing, dewarping, noise reduction).  
- **[Pytesseract]** → to perform OCR on the processed images.  

The extracted text is further processed, cleaned, and stored for downstream use.

---

## ⚙️ Features
- Convert PDF pages into images with configurable DPI.  
- Preprocess images (deskew, resize, denoise) for better OCR accuracy.  
- Extract raw text using Tesseract OCR.  
- Option to save extracted text into structured formats (`.txt`, `.json`, or database).  
- Support for experimentation via **branches** (testing new features without breaking `main` or `master`).  

---

## 🏗️ Project Structure  
PROJECT_5_DATA_EXTRACTION_FROM_PDF_USING_OCR/  
│
├── codebase/ # Main source code  
│ ├── main.py # Entry point  
│ ├── utils/ # Helper modules  
│ │ ├── paths.py # Directory paths, constants  
│ │ ├── preprocess.py # Image preprocessing functions (OpenCV)  
│ │ ├── ocr.py # OCR wrapper functions  
│ │ └── pdf_utils.py # PDF-to-image conversion utilities (PyMuPDF)  
│
├── document.pdf # Sample input PDF  
├── requirements.txt # Python dependencies  
├── README.md # Project documentation (this file)  
└── RESULT/ # Output folder (OCR results, JSON, etc.)  