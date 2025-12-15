import cv2
import os
import csv
from ocr.tesseract_ocr import run_tesseract
from ocr.easyocr_ocr import run_easyocr
from ocr.paddleocr_ocr import run_paddleocr

comparison_results = []

# Image Processing
def preprocess_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image not found. Check the image path")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    return thresh

#Helper function to save outputs

def save_output(engine_name, image_name, text, time_taken):
    os.makedirs("output", exist_ok=True)

    file_path = f"output/{engine_name}_output.txt"
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"\n=== IMAGE: {image_name} ===\n")
        f.write(f"Time taken: {time_taken:.2f} seconds\n")
        f.write("Extracted Text:\n")
        f.write(text)
        f.write("\n" + "-" * 50 + "\n")

        #Save Comparison Table To CSV
def save_comparison_table(results):
    os.makedirs("output", exist_ok=True)
    file_path = "output/ocr_comparison.csv"
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["image", "engine", "time"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\n Comparison tables saved to {file_path}")

# Main execution
if __name__ == "__main__":

    images_folder = "images"

    for image_name in os.listdir(images_folder):

        if image_name.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(images_folder, image_name)

            print(f"\n Processing: {image_name}")

# Preprocess image

            processed_img = preprocess_image(image_path)

# Run Tesseract OCR Engines
            tess_text, tess_time = run_tesseract(processed_img)
            easy_text, easy_time = run_easyocr(image_path)
            paddle_text, paddle_time = run_paddleocr(image_path)

            print("\n--- TESSERACT OUTPUT ---")
            print(tess_text)
            print("Time taken:", tess_time)

            print("\n--- EASYOCR OUTPUT ---")
            print(easy_text)
            print("Time taken:", easy_time)

            print("\n--- PADDLEOCR OUTPUT ---")
            print(paddle_text)
            print("Time taken:", paddle_time)

            # Store Results During Processing
            comparison_results.append({
                "image": image_name,
                "engine": "Tesseract",
                "time": round(tess_time, 2)
            })

            comparison_results.append({
                "image": image_name,
                "engine":  "EasyOCR",
                "time": round(easy_time, 2)
            })

            comparison_results.append({
                "image": image_name,
                "engine": "PaddleOCR",
                "time": round(paddle_time, 2)
            })

        # Saves Comparison results
        save_comparison_table(comparison_results)


        # Save outputs
        save_output("tesseract", image_name, tess_text, tess_time)
        save_output("easyocr", image_name, easy_text, easy_time)
        save_output("paddleocr", image_name, paddle_text, paddle_time)