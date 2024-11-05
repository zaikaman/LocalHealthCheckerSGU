import os
from PIL import Image
import pytesseract

os.environ["TESSDATA_PREFIX"] = "/app/tessdata/"

def extract_text_from_image(filepath, lang='vie'):
    """Extract text from an image file using Tesseract OCR."""
    image = Image.open(filepath)
    text = pytesseract.image_to_string(image, lang=lang)
    return text
