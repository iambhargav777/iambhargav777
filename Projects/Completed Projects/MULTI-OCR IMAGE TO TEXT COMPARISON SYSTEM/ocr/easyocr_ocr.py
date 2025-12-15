import time
import easyocr

# Load OCR Models
easy_reader = easyocr.Reader(['en'])

# EasyOCR function

def run_easyocr(image_path):
    start_time = time.time()
    results = easy_reader.readtext(image_path)
    text = " ".join([res[1] for res in results])
    duration = time.time() - start_time
    return text, duration
