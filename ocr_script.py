from PIL import Image, ImageEnhance
import pytesseract
import cv2
import numpy as np
import re

# Set path to Tesseract (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load and preprocess image
image = Image.open("fld.png").convert("L")
image = ImageEnhance.Contrast(image).enhance(2.5)
open_cv_image = np.array(image)

# Thresholding
_, thresh = cv2.threshold(open_cv_image, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Resize
scaled = cv2.resize(thresh, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

# OCR with custom config
raw_text = pytesseract.image_to_string(scaled, config="--psm 6")

print("Full OCR Text:\n")
print(raw_text)

# Save full text for reference
with open("fld_extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(raw_text)

# --- Field Extraction ---
fields = {}

# DLN (Driver License Number)
dln_match = re.search(r'S\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{3}[- ]?\d?', raw_text)
fields["DLN"] = dln_match.group(0) if dln_match else "Not found"

# Name
name_match = re.search(r'SAMPLE\s*\nNICK', raw_text, re.IGNORECASE)
fields["Name"] = "NICK SAMPLE" if name_match else "Not found"

# Address
addr_match = re.search(r'123 MAIN.*TALLAHASSEE.*', raw_text, re.IGNORECASE)
fields["Address"] = addr_match.group(0) if addr_match else "Not found"

# DOB
dob_match = re.search(r'0[1-9]/[0-3][0-9]/19[0-9]{2}', raw_text)
fields["DOB"] = dob_match.group(0) if dob_match else "Not found"

# EXP (Expiration Date)
exp_match = re.search(r'EXP.*?(\d{2}/\d{2}/\d{4})', raw_text)
fields["EXP"] = exp_match.group(1) if exp_match else "Not found"

# SEX
sex_match = re.search(r'SEX[: ]*([MF])', raw_text)
fields["SEX"] = sex_match.group(1) if sex_match else "Not found"

# HEIGHT
height_match = re.search(r'HEIGHT[: ]*(\d[\'’][0-9]{1,2})', raw_text)
fields["Height"] = height_match.group(1) if height_match else "Not found"

# Safe Driver Date
safe_driver_match = re.search(r'SAFE DRIVER\s+(\d{2}/\d{2}/\d{4})', raw_text)
fields["Safe Driver Since"] = safe_driver_match.group(1) if safe_driver_match else "Not found"

# --- Output Results ---
print("\n--- Extracted Fields ---")
for key, value in fields.items():
    print(f"{key}: {value}")

# Save boxed image for visual debugging
cv2.imwrite("fld_processed.png", scaled)
