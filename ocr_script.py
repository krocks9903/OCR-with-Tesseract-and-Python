from PIL import Image, ImageFilter, ImageOps, ImageDraw
import pytesseract
from pytesseract import Output
import re
import matplotlib.pyplot as plt

# Load image
image_path = "JC.jpg"
img = Image.open(image_path)

# --- Image Preprocessing ---
img = img.convert("L")  # Convert to grayscale
img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150))  # Sharpen
img = img.point(lambda x: 255 if x > 140 else 0, mode='1')  # Binarize
img = img.resize((img.width * 2, img.height * 2))  # Upscale for better OCR

# --- Run OCR and get word-level data ---
ocr_data = pytesseract.image_to_data(img, config='--psm 6', output_type=Output.DICT)
ocr_text = pytesseract.image_to_string(img, config='--psm 6')

# --- Extract DLN, Name, Address using regex ---
dln_match = re.search(r'\b[S|W]?\d{3}-\d{3}-\d{2}-\d{3}-?\d?\b', ocr_text)
name_match = re.search(r'([A-Z]+)\s+([A-Z]+)', ocr_text)
address_match = re.search(r'(\d+\s+.+\s+TALLAHASSEE,\s*FL.*?)\n', ocr_text, re.IGNORECASE)

dln = dln_match.group(0) if dln_match else "Not found"
name = f"{name_match.group(1).title()} {name_match.group(2).title()}" if name_match else "Not found"
address = address_match.group(1).title() if address_match else "Not found"

# --- Print Extracted Info ---
print("\n--- OCR Results ---")
print(f"DLN: {dln}")
print(f"Name: {name}")
print(f"Address: {address}")

# --- Draw bounding boxes on words with > 50% confidence ---
img_with_boxes = img.convert("RGB")
draw = ImageDraw.Draw(img_with_boxes)

for i in range(len(ocr_data['text'])):
    try:
        if float(ocr_data['conf'][i]) > 50:
            x, y, w, h = ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i]
            draw.rectangle([x, y, x + w, y + h], outline="red", width=2)
    except ValueError:
        continue

# --- Save output image ---
output_path = "ID_bounding_boxes_saved.png"
img_with_boxes.save(output_path)
print(f"\n✅ Saved: {output_path}")
