import time
import pytesseract

# Set Tesseract Path (Windows)

pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")

# Tesseract OCR function

def run_tesseract(processed_image):
    start_time = time.time()
    text = pytesseract.image_to_string(processed_image)
    duration = time.time() - start_time
    return text, duration
