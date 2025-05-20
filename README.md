# OCR-with-Tesseract-and-Python

This project is an AI-powered OCR tool that extracts key information (e.g., Name, Date of Birth, ID Number) from scanned images of passports and driver's licenses and stores them in a structured database.

---

## Project Overview

OCR-with-Tesseract-and-Python is a Python-based optical character recognition (OCR) system designed to extract structured data from official identification documents such as driver's licenses and passports. The project uses Tesseract OCR along with a preprocessing pipeline to improve accuracy on real-world scanned images.

---

## Features

- Extracts fields such as:
  - Full Name
  - Date of Birth (DOB)
  - ID Number / Driver License Number (DLN)
  - Address
- Supports multiple image formats (PNG, JPG, TIFF)
- Applies image preprocessing to improve OCR accuracy
- Field-specific cropping for better performance
- Outputs structured data (JSON, CSV)
- Easily extendable for new ID formats

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

```json
{
  "DLN": "7F62-4A3-G9-0W7-5",
  "Name": "Jeremiah Cedar",
  "Address": "3351 Bagwell Avenue, Bogsville, FL 34448",
  "DOB": "03/03/1989",
  "EXP": "03/03/2024"
}
