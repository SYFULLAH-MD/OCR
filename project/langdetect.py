import cv2
import pytesseract
from langdetect import detect
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Lenovo\Desktop\Tesseract-OCR\tesseract.exe'
img = cv2.imread(r"C:\Users\Lenovo\PycharmProjects\TextDect\Tesseract-OCR\w.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
iden = pytesseract.image_to_string(img)
print(detect(iden))
cv2.imshow('res', img)
cv2.waitKey(0)
