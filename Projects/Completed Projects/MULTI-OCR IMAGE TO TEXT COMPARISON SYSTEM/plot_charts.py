import os
import pandas as pd
import matplotlib.pyplot as plt

#Create Chart folder
CHARTS_DIR = "output/charts"
os.makedirs(CHARTS_DIR, exist_ok=True)

#Load CSV file
csv_path = "output/ocr_comparison.csv"
df = pd.read_csv(csv_path)

print(df.head()) #sanity check

# Chart 1 : Average Time per OCR

avg_time = df.groupby("engine")["time"].mean()

plt.figure()
avg_time.plot(kind="bar")
plt.xlabel("OCR Engine")
plt.ylabel("Avergae Time (seconds)")
plt.title("Average OCR Execution Time by Engine")
plt.tight_layout()

plt.savefig(f"{CHARTS_DIR}/avg_execution_time.png")
plt.show()
plt.close()

#Chart 2 : OCR Time per Image
for engine in df["engine"].unique():
    engine_df = df[df["engine"] == engine]

    plt.figure()
    plt.plot(engine_df["image"], engine_df["time"], marker="o")
    plt.xlabel("Image")
    plt.ylabel("Time (seconds)")
    plt.title(f"{engine} OCR Time per Image")
    plt.xticks(rotation=45)
    plt.tight_layout()

    file_name = f"execution_time_per_image_{engine.lower()}.png"
    plt.savefig(f"{CHARTS_DIR}/{file_name}")
    plt.show()
    plt.close()

print("Charts saved successfully in output/charts/")