import os
import sys

# 1. Setup the paths so the files can see each other
current_dir = os.getcwd()
reading_dir = os.path.join(current_dir, "reading")
sys.path.append(current_dir)
sys.path.append(reading_dir)

# 2. Import the LOAD function and MusicRender class
try:
    # Based on your file uploads, load() is a function in music.py
    from reading.music import load, MusicRender
    print("✅ Successfully imported load and MusicRender!")
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("Try ensuring you are running this from C:\\Users\\zelen\\PDMX")
    sys.exit()

# 3. Path to your specific JSON file
json_path = r"pdmx_data\data\10\32\QmSMz3VBJ1CzVP3UZJrbwRJhSRRYNuP75qSvvbS3R3MRYv.json"

if os.path.exists(json_path):
    # 4. Use the standalone load() function
    print(f"Reading file: {json_path}...")
    score = load(json_path)
    
    print(f"🎵 Successfully loaded: {score.metadata.title}")

    # 5. Export to MusicXML
    # This creates the 'Answer Key' for your OMR model
    output_xml = "pdmx_result.musicxml"
    score.write(output_xml)
    print(f"🚀 Success! Created {output_xml}")
else:
    print(f"❌ Could not find the JSON file at {os.path.abspath(json_path)}")