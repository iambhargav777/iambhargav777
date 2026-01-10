import time
from paddleocr import PaddleOCR

# Initialize PaddleOCR ONCE (modern & safe)
paddle_reader = PaddleOCR(use_angle_cls=True,lang="en")

def run_paddleocr(image_path):
    start = time.time()

    results = paddle_reader.ocr(image_path)
    items = []

    # PaddleOCR returns nested list → results[0]
    if results and len(results) > 0:
        for line in results[0]:
            bbox = line[0]              # coordinates
            text = line[1][0]           # recognized text

            # use top-left corner for ordering
            x = bbox[0][0]
            y = bbox[0][1]
            items.append((y, x, text))

    # Sort by reading order
    items.sort()

    lines = []
    current_line = []
    last_y = None
    y_threshold = 15

    for y, x, text in items:
        if last_y is None or abs(y - last_y) < y_threshold:
            current_line.append(text)
        else:
            lines.append(" ".join(current_line))
            current_line = [text]

        last_y = y

    if current_line:
        lines.append(" ".join(current_line))

    final_text = "\n".join(lines)
    return final_text, time.time() - start
