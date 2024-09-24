from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
'''import mysql.connector as sql

mydb = sql.connect(host='localhost', user='root', password='tiger', database='Details')
my= mydb.cursor()
my.execute("show databases")

LARGEFONT=("Verdana", 35)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.parent = parent
        self.parent.title("Library Management System")
        self.parent.geometry("1910x1000+0+0")

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, LMS):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(LMS))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)'''

class LMS():
    def __init__(self, root):

        #tk.Frame.__init__(self, root)
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1910x1000+0+0")
        self.root.state('zoomed')
        #Ryan_logo= PhotoImage(file="Ryanlogo.jpg", master=root)

        #imageFile= "Ryanlogo.jpg"
        #root.im1= Image.open(imageFile)

        #path="Ryanlogo.jpg"
        #img= ImageTk.PhotoImage(Image.open(path))

        #panel.pack(side="bottom", fill= "both", expand="yes")

        #header = Label(self.root, bg="#8B8682", bd=50, padx=0, pady=0)
        #header.pack(side=TOP, fill=X)

        #ryan details removed
        "==============================================================TOP FRAME=========================================================================================================================="
        header = Frame(self.root, bg="#8B8682", bd=50, padx=0, pady=0)
        header.place(x=0, y=0, width=1910, height=165)

        image1 = Image.open("Ryan_International_Group_logo.jpg")
        test = ImageTk.PhotoImage(image1)

        label1 = Label(image=test)
        label1.image = test

        label1.place(x=0, y=0, width=200, height=165)

        #lbltitle=Label(self.root, text="RYAN INTERNATIONAL SCHOOL", bg="#CDC5BF", fg='#FFF5EE', bd=10, relief=RIDGE, font=("times new roman", 50, "bold"),  padx=0, pady=20,)
        #lbltitle.pack(side=TOP, fill=X)

        #RyanName=Label(header, text="RYAN INTERNATIONAL SCHOOL", bg="#CDC5BF", fg='#FFF5EE', bd=10, relief=RIDGE, font=("times new roman", 40, "bold"), padx=30, pady=0)
        #RyanName.place(x=60, y=80, width=1800, height=120)       #not extendinf on the negative STUDENT_DETAILS axis, can be used for ryan logo


        "===================================================MIDDLE FRAME======================================================================================================================="
        middleframe=Frame(self.root, bd=12, padx=20, bg="#FFFF00")
        middleframe.place(x=450, y=250, width=743, height=600)

        middleframe2=LabelFrame(middleframe, text="ISSUE DETAILS", bd=5, relief=RAISED, font=("arial italic",20), padx=20, bg="#DCDCDC")
        middleframe2.place(x=-10, y=10, width=700, height=500)

        lblmember=Label(middleframe2, bg="#C1C1C1", text="Member", font=("times new roman", 28,"bold"),padx=140, pady=0)
        lblmember.grid(row=1, column=0, sticky=W)

        comMember=ttk.Combobox(middleframe2, font=("ariel", 20), width=11, state="readonly")
        comMember["value"]=("Admin","Staff", "Student")
        comMember.grid(row=1, column=1)

        lbladmission_no = Label(middleframe2, bg="#C1C1C1", text="Admission Number", font=("times new roman", 28, "bold"), padx=55, pady=0)
        lbladmission_no.grid(row=2, column=0, sticky=W)

        txtadmission_no=Entry(middleframe2, font=("times new roman", 20, "bold"), width= 13)
        txtadmission_no.grid(row=2, column=1)

        lblbook_code = Label(middleframe2, bg="#C1C1C1", text="Book Code", font=("times new roman", 28, "bold"), padx=121, pady=0)
        lblbook_code.grid(row=3, column=0, sticky=W)

        txtbook_code = Entry(middleframe2, font=("times new roman", 20, "bold"), width=13)
        txtbook_code.grid(row=3, column=1)

        next_button = Button(middleframe2, text="NEXT", padx=85, pady=10, borderwidth=3, bg="#008B8B")
        next_button.grid(row=4, column=1)



        "==================================================RIGHT SIDE FRAME========================================================================================================================="
        rightframe = Frame(self.root, bd=12, padx=100, bg="blue")
        rightframe.place(x=1215, y=250, width=603, height=600)

        #lbldetails= Label(rightframe, bg="#C1C1C1", text="CONFORAMTION DETAILS", bd=5, font=("MS Gothic", 30, "bold"), padx=100, pady=20)
        #lbldetails.grid(row=5, column=5, sticky=W)

        rightframe2 = LabelFrame(rightframe, text="CONFIRMATION", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
        rightframe2.place(x=-90, y=10, width=560, height=500)

        self.txtBox=Text(rightframe2, font=("arial", 15, "bold"), width=18, height=7, padx=149, pady=50)
        self.txtBox.grid(row=0, column=0, columnspan=2)

        #deaitls that need to be shown= admission number. name calss sec, book code name author
        '''if txtadmission_no in my:
            idk_button=Button(middleframe2, text="IDK", padx=145, pady=10, borderwidth=3, bg="#008B8B")
            idk_button.grid(row5, column1)
            #self.txtBox.insert(END, #HOW TO ADD DATA FROM ADMISSION NUMBER?? AND BOOK CODE )'''

        confirm_button=Button(rightframe2, text="CONFIRM", padx=96, pady=20, borderwidth=3, bg="#8EE5EE")
        confirm_button.grid(row=1, column=0)

        cancel_button = Button(rightframe2, text="CANCEL", padx=95, pady=20, borderwidth=3, bg="#53868B")
        cancel_button.grid(row=1, column=1)

        #code to show the deatils according to data entered#
        #"Terminal" font>>> gaming kinda


        "==================================================LEFT SIDE FRAME=========================================================================================================================="
        leftframe=Frame(self.root, bd=12, padx=0, bg="#5B5B5B")
        leftframe.place(x=0, y=165, width=200, height=800)

        #e=LabelFrame(Entry(root, width=50, borderwidth=7, bg="black"))

if __name__ == "__main__":
    root=Tk()
    #app=tkinterApp()
    obj=LMS(root)
    root.mainloop()

