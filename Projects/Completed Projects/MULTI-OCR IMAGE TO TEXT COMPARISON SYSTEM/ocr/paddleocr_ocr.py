import time
from paddleocr import PaddleOCR

# Load OCR Models
paddle_reader = PaddleOCR(use_angle_cls=True, lang='en')

# PaddleOCR function

def run_paddleocr(image_path):
    start_time = time.time()
    results = paddle_reader.ocr(image_path)
    text = ""
    if results and results[0]:
        text = " ".join([line[1][0] for line in results[0]])

    duration = time.time() - start_time
    return text, duration
