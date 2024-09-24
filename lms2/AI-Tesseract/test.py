'''import cv2
from PIL import Image
from pytesseract import pytesseract

camera = cv2.VideoCapture(0)

while True:
    _,Image = camera.read()
    cv2.imshow('Text Detection', Image)
    #if cv2.waitkey(1) & 0*FF==ord('s'):
    #    cv2.imwrite('test1.jpg', Image)
    #    break
camera.release()
cv2.destoryAllWindows()

def tesseract():
    path_to_tesseract=r""
    Image_path = 'test1.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text)
tesseract()'''

import pytesseract
import cv2
#img = cv2.imread('bruh.jpg')
#img = cv2.resize(img, (600, 360))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#print(pytesseract.image_to_string(img))
#cv2.imshow('Result', img)
# cv2.waitKey(0)
# from pytesseract import pytesseract

#pytesseract.tesseract_cmd=  "C:\\Users\\admin\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\site-packages\\pytesseract"

img = cv2.imread("bruh1.png")

words_in_image = pytesseract.image_to_string(img)
print(words_in_image)