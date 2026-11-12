# OCR-with-Tesseract-and-Python

Extracts the licence number, name and address from a scanned driver's licence image using Tesseract OCR, image preprocessing and regular expressions.

> **Status:** single-script prototype (`ocr_script.py`), tuned on one sample Florida licence image (`fld.png`). It prints the extracted fields to the console and saves an image with word bounding boxes. It does not write JSON, CSV or a database yet, and it has not been tested on passports. The sections below describe the design and where it is headed; items marked *planned* are not implemented.

---

## Project Overview

OCR-with-Tesseract-and-Python is a Python-based optical character recognition (OCR) system designed to extract structured data from official identification documents such as driver's licenses and passports. The project uses Tesseract OCR along with a preprocessing pipeline to improve accuracy on real-world scanned images.

---

## Features

- Extracts fields such as:
  - Full Name
  - Date of Birth (DOB) *(planned)*
  - ID Number / Driver License Number (DLN)
  - Address
- Reads any image format Pillow can open (tested with PNG)
- Applies image preprocessing to improve OCR accuracy
- Field-specific cropping for better performance
- Structured output (JSON, CSV) *(planned; currently prints to console)*
- New ID formats need new regex patterns and crop regions

---

## Tech Stack

| Tool           | Purpose                                 |
|----------------|-----------------------------------------|
| Python         | Core scripting language                 |
| Pillow (PIL)   | Image loading and preprocessing         |
| pytesseract    | Python wrapper for Tesseract OCR engine |
| Tesseract OCR  | Open-source text recognition engine     |
| regex          | Pattern-based field extraction          |
| matplotlib     | (Optional) Visualization of bounding boxes |

---

## How It Works

1. Load a scanned image of an ID or passport
2. Apply grayscale, sharpening, binarization, and resizing
3. (Optionally) crop regions like DLN, Name, DOB
4. Run OCR using Tesseract on the full image or cropped sections
5. Use regex to extract meaningful fields
6. Print or store the results in a structured format

---

## Example Output

Target output format. The script currently prints the DLN, name and address fields as plain text.

```json
{
  "DLN": "7F62-4A3-G9-0W7-5",
  "Name": "Jeremiah Cedar",
  "Address": "3351 Bagwell Avenue, Bogsville, FL 34448",
  "DOB": "03/03/1989",
  "EXP": "03/03/2024"
}
