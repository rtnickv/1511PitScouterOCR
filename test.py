from PIL import Image
from pytesseract import pytesseract

img_path = "/Users/nickvessa/1511PitScouterOCR/sample_test_imgs/0*HGgKcW4a9sHMZJDr.webp"

img = Image.open(img_path)

text = pytesseract.image_to_string(img)

print(text)