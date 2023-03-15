from PIL import Image
from pytesseract import pytesseract

img_path = "/Users/nickvessa/1511PitScouterOCR/sample_test_imgs/1601120C-1DD4-4D80-A7A8-C2D531D3ABFE.jpeg"

img = Image.open(img_path)

text = pytesseract.image_to_string(img)

print(text)