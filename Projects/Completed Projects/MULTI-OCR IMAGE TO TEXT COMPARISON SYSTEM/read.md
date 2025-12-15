Python Version Requirement (IMPORTANT)

This project must be run using Python 3.10.

EasyOCR has compatibility issues with newer Python versions (3.11+).
Use Python 3.10 only.

Setup Instructions

1.Create Virtual Environment (Python 3.10)

python -m venv .venv


Activate:
.venv\Scripts\activate

2.Install Dependencies

pip install pytesseract easyocr paddleocr opencv-python pandas matplotlib

OR 

Use file requirements.txt 

3.Install Tesseract OCR Engine (Required)

Tesseract OCR must be installed separately.

Windows:

Download from:
https://github.com/UB-Mannheim/tesseract/wiki

Install Tesseract OCR

Default installation path:

C:\Program Files\Tesseract-OCR\tesseract.exe


Ensure this path is configured in the code:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

OCR Engines

Tesseract OCR – Fast, traditional OCR

EasyOCR – Deep learning-based, higher text coverage

PaddleOCR – Advanced OCR for structured documents

Key Features:

Batch image processing

OpenCV-based image preprocessing

Modular OCR design

Execution-time benchmarking

CSV performance report

Automatic chart generation

How It Works:

Read images from folder

Preprocess images

Run OCR engines independently

Measure execution time

Store results (TXT, CSV)

Generate performance charts

Run Instructions:

python multi_ocr.py

python plot_charts.py

Output:

OCR text files

ocr_comparison.csv

Execution-time charts (output/charts/)