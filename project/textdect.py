import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR.tesseract.exe'
img = cv2.imread(r'C:\Users\Lenovo\Desktop\ocr\damn.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
cv2.imshow('res',img)
cv2.waitKey(0)
