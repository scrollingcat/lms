import cv2
from pytesseract import pytesseract
# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
cam_port = 0
cam = cv2.VideoCapture(cam_port)

# reading the input using the camera
result, image = cam.read()

# If image will detected without any error,
# show result
if result:

    # showing result, it take frame name and image
    # output
    cv2.imshow("GeeksForGeeks", image)

    # saving image in local storage
    cv2.imwrite("GeeksForGeeks.png", image)

    # If keyboard interrupt occurs, destroy image
    # window
    cv2.waitKey(500)
    cv2.destroyWindow("GeeksForGeeks")



    pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


    words_in_image = pytesseract.image_to_string(image)

    print(words_in_image)


# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")