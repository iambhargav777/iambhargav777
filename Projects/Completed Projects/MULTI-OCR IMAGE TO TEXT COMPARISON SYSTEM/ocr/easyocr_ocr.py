import time
import easyocr

# Load OCR Models
easy_reader = easyocr.Reader(['en'], gpu=False)

def run_easyocr(image_path):
    start_time = time.time()

    # detail=1 → bbox + text + confidence
    results = easy_reader.readtext(image_path, detail=1)

    # Sort top-to-bottom, left-to-right
    results = sorted(results, key=lambda r: (r[0][0][1], r[0][0][0]))

    lines = []
    current_line = []
    last_y = None
    y_threshold = 15  # line grouping tolerance

    for bbox, text, conf in results:
        y = bbox[0][1]

        if last_y is None or abs(y - last_y) < y_threshold:
            current_line.append(text)
        else:
            lines.append(" ".join(current_line))
            current_line = [text]

        last_y = y

    if current_line:
        lines.append(" ".join(current_line))

    final_text = "\n".join(lines)
    duration = time.time() - start_time
    return final_text, duration
