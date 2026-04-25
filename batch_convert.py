import os
import subprocess
from pathlib import Path

# 1. Configuration
MUSESCORE_PATH = r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"
INPUT_DIR = Path(r"C:\Users\zelen\PDMX\output_xmls")
OUTPUT_DIR = Path(r"C:\Users\zelen\PDMX\output_pdfs")

# Create output folder if it doesn't exist
OUTPUT_DIR.mkdir(exist_ok=True)

def convert_to_pdf(xml_path):
    # Construct the output filename
    pdf_path = OUTPUT_DIR / xml_path.with_suffix(".pdf").name
    
    print(f"Converting: {xml_path.name} -> {pdf_path.name}")
    
    # The magic command
    # -o tells MuseScore where to save the output
    command = [MUSESCORE_PATH, "-o", str(pdf_path), str(xml_path)]
    
    try:
        subprocess.run(command, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to convert {xml_path.name}: {e}")

# 2. Execution loop
xml_files = list(INPUT_DIR.glob("*.musicxml"))
print(f"Found {len(xml_files)} files to process.")

for file in xml_files:
    convert_to_pdf(file)

print("✅ Batch processing complete!")