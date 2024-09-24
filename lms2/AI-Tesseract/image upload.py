import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window
my_w.title('www.plus2net.com')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Add Student Data with Photo',width=30,font=my_font1)
l1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Upload File',
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1)

def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    img_resized=img.resize((400,200)) # new width & height
    img=ImageTk.PhotoImage(img_resized)
    b2 =tk.Button(my_w,image=img) # using Button
    b2.grid(row=3,column=1)
    import pytesseract
    import cv2
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img1 = cv2.imread(filename)

    words_in_image = pytesseract.image_to_string(img1)
    print(words_in_image)
my_w.mainloop()  # Keep the window open
