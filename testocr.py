from PIL import Image
import pytesseract

path = r"C:\Users\Corey\Downloads\sour.png"
pytesseract.image_to_string(Image.open(path))


