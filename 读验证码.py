#coding = utf-8
import pytesseract
from PIL import Image

image = Image.open("C:/Users/高泽静/PycharmProjects/test/bg_img/imooc2.png")
text = pytesseract.image_to_string(image)
print(text)