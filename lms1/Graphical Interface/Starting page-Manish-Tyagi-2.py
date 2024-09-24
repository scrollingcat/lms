from warning_email import *
from record_no_finder import *
from admission_no_finder import *
from book_search import *
from student_list import *
from delete import *
from issue_record_show import show_all_records
from Extension import *
from book_return import *
from issue_records import *
from show_books import show_all_books
from book_update_new import *
from Adding_Books import addbooks
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pytesseract
import cv2

#TODO : issue reocrd, update show book, delete book, student list

def temp_text1(e):
   txtsearch.insert(0,"Search")

def temp_txt(e):
   txtsearch.delete(0,"end")

def show_frame(frame):
    frame.tkraise()

'''def delete_entry():
   e= txtsearch.get()
   e.delete(0,END)'''

def show_password():
   if entry.cget("show")=='*':
      entry.config(show= '')
   else:
      entry.config(show='*')

window = tk.Tk()
window.geometry("1910x1000+0+0")
window.state('zoomed')
window.title("Library Management System")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

mainframe = tk.Frame(window)
issue = tk.Frame(window)
issue_confirmation = tk.Frame(window)
search = tk.Frame(window)
frame5 = tk.Frame(window)    #RETURN 1st page of deatils
frame6 = tk.Frame(window)    #EXTENTSION 1st page
frame7 = tk.Frame(window)    #RECORD 1st page
frame8 = tk.Frame(window)    #STOCK 1st page
frame9 = tk.Frame(window)    #ISSUE 2nd page confirmation details
frame10 = tk.Frame(window)   #RETURN 2nd page confirmation details
frame11 = tk.Frame(window)   #RETURN 3rd page return confirmation
frame12 = tk.Frame(window)   #EXTENTION 2nd page confirmation details
frame13 = tk.Frame(window)   #EXTENTION 3rd page extention confirmation
frame14 = tk.Frame(window)   #SHOW BOOKS 1st page
frame15 = tk.Frame(window)   #ADD BOOKS 1st page
frame16 = tk.Frame(window)   #UPDATE BOOKS 1st page
frame17 = tk.Frame(window)   #DELETE BOOKS 1st page
frame18 = tk.Frame(window)   #STUDENT LIST 1st page
frame19 = tk.Frame(window)   #ADD BOOKS confirmation
frame20 = tk.Frame(window)   #UPDATE BOOKS 2nd page book  data
frame21 = tk.Frame(window)   #UPDATE BOOKS 3rd page confirmation
frame22 = tk.Frame(window)   #DELETE details
frame23 = tk.Frame(window)   #DELETE confirmation
frame24 = tk.Frame(window)   #SEARCH page 2


bg = PhotoImage(file="Images/Illustration2.png")
my_label=Label(mainframe, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

search['bg']= '#101014'

for frame in (mainframe, issue, issue_confirmation, search, frame5, frame6, frame7, frame8, frame9, frame10, frame11, frame12, frame13, frame14, frame15, frame16, frame17, frame18, frame19, frame20, frame21, frame22, frame23, frame24):
    frame.grid(row=0, column=0, sticky='nsew')
"==============================================================MAIN FRAME=========================================================================================================================="
txtsearch=Button(mainframe, text= "Search...                                                                                                                                                         ", font=('arial', 20), bg="white", width= 80, height= 0, command=lambda: show_frame(search))
txtsearch.place(x= 250, y=400)
#txtsearch.bind("<FocusIn>", temp_txt)

txtsearch=Button(mainframe, text= "Photo", font=('arial', 20), bg="white", width= 10, height= 0, command=lambda: show_frame(search))
txtsearch.place(x= 400, y=400)

frame1_insert = tk.Button(mainframe, text='ISSUE', fg='white', command=lambda: issuef(), bg="#1E1E20", padx=200, pady=20)
frame1_insert.place(x=150, y=750)

frame1_return = tk.Button(mainframe, text='RETURN',fg='white', command=lambda: returnf(), bg="#1E1E20", padx=200, pady=20)
frame1_return.place(x=738, y=750)

frame1_extention = tk.Button(mainframe, text='EXTENTION',fg='white', command=lambda: extentionf(), bg="#1E1E20", padx=200, pady=20)
frame1_extention.place(x=1300, y=750)


def issued_records():
   show_all_records()
   ii = show_all_records()
   i=0
   for tiger in ii:
      #print (tiger)
      for j in range (len(tiger)):
         e = Label(txtBox_issuerecord, width=10, text=tiger[j])
         e.grid(row=i, column=j)
      i+=1

#reccord no., addmission no, book code, issue date, reutrn date, final return date, reutrn status
frame1_record = tk.Button(mainframe, text='RECORDS',fg='white', command=lambda: [issued_records(),show_frame(frame7)], bg="#1E1E20", padx=200, pady=20)
frame1_record.place(x=440, y=840)

frame1_stock = tk.Button(mainframe, text='STOCK',fg='white', command=lambda: show_frame(frame8), bg="#1E1E20", padx=200, pady=20)
frame1_stock.place(x=1020, y=840)

"==================================================FRAME 4(SEARCH OPTIONS)=========================================================================================================================="
bg_search = PhotoImage(file="Images/Illustration6.png")
search_label=Label(search, image=bg_search)
search_label.place(x=0, y=0, relwidth=1, relheight=1)

comSearch=ttk.Combobox(search, font=("helvetica", 34), width=14, state="readonly")
comSearch["value"]=("Book","Records", "Admission No.", "Photo Upload")
comSearch.place(x=275, y=425)

txtsearch=Entry(search, font=('helvetica', 34), fg="#44444B", width=56)
txtsearch.insert(0, "Search")
#txtsearch.place(x= 500, y=440)  font 100   bg="#aaa9ad",
txtsearch.place(x= 275, y=500)
txtsearch.bind("<FocusIn>", temp_txt)
txtsearch.bind("<FocusOut>", temp_text1)

search_button = Button(search, text="GO", fg="white", padx=85, pady=10, borderwidth=3, bg="#1E1E20", command= lambda: search1())
search_button.place(x=1485, y=575)

frame4_backbutton = tk.Button(search, command=lambda: show_frame(mainframe), bg="white", padx=40, pady=20)
frame4_backbutton.place(x=10, y=10)

def search1():
   Search=comSearch.get()
   searchbar = txtsearch.get()
   if not Search or not searchbar:
      Label(search, text="Arey kuch toh enter karo", font=('Century 15 bold')).pack(pady=20)
   elif Search=="Book":
      searched_name=search_book(searchbar)
      if searched_name==0:
         Label(frame24, text="Hamare paas yeh book nahi nahi\nwould you like to search it up online?", font=('Century 15 bold')).pack(pady=300)
         
         google_button = Button(frame24, text="GOOGLE", fg="white", padx=200, pady=20, borderwidth=3, bg="#1E1E20", command=lambda: online_search("Google",searchbar))
         google_button.place(x=150, y=500)

         amazon_button = Button(frame24, text="AMAZON", fg="white", padx=200, pady=20, borderwidth=3, bg="#1E1E20", command=lambda: online_search("Amazon",searchbar))
         amazon_button.place(x=738, y=500)

         flipkart_button = Button(frame24, text="FLIPKART", fg="white", padx=200, pady=20, borderwidth=3, bg="#1E1E20", command=lambda: online_search("Flipkart",searchbar))
         flipkart_button.place(x=1000, y=500)

      else:
         ii = searched_name
         i = 0
         for tiger in ii:
            #print (tiger)
            for j in range(len(tiger)):
               e = Label(frame24, width=13, text=tiger[j])
               e.grid(row=i, column=j)
            i += 1
      show_frame(frame24)
   elif Search=="Records":
      searched_record=record_no_finder(searchbar)
      if searched_record==0:
         Label(search, text="No record found",font=('Century 15 bold')).pack(pady=20)
      else:
         details_of_student=searched_record[0]
         name_of_student="Name of Student : "+details_of_student[0]
         class_of_student="Class : "+str(details_of_student[1])+details_of_student[2]

         Label(frame24, text= name_of_student).place(x=100, y=200)
         Label(frame24, text=class_of_student).place(x=500, y=200)
         details_of_record=searched_record[1]
         ii = details_of_record
         i = 0
         for tiger in ii:
            # print (tiger)
            for j in range(len(tiger)):
               e = Label(frame24, width=13, text=tiger[j])
               e.grid(row=i, column=j)
            i += 1
         show_frame(frame24)
   elif Search=="Admission No.":
      searched_no=admission_no_finder(searchbar)
      if searched_no==0:
         Label(search, text="Not Found", font=('Century 15 bold')).pack(pady=20)
      else:
         ii = searched_no
         i = 0
         for tiger in ii:
            # print (tiger)
            for j in range(len(tiger)):
               e = Label(frame24, width=13, text=tiger[j])
               e.grid(row=i, column=j)
            i += 1
   elif Search=="Photo Upload":
      b1 = tk.Button(search, text='Upload File',
                     width=20, command=lambda: upload_file())
      b1.grid(row=1, column=1)

      def upload_file():
         global img
         f_types = [('Jpg Files', '*.jpg')]
         filename = filedialog.askopenfilename(filetypes=f_types)
         img = Image.open(filename)
         img_resized = img.resize((400, 200))  # new width & height
         img = ImageTk.PhotoImage(img_resized)
         b2 = tk.Button(search, image=img)  # using Button
         b2.grid(row=3, column=1)

         pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
         img1 = cv2.imread(filename)

         words_in_image = pytesseract.image_to_string(img1)
         print(words_in_image)
         show_frame(frame24)

   #Label(issue, text=seacrhbar, font= ('Century 15 bold')).pack(pady=20)
   #txtsearch.delete(0, END)

"==================================================FRAME 24(SEARCH RESULT)=========================================================================================================================="
bg_search1 = PhotoImage(file="Images/Illustration6.png")
search1_label=Label(frame24, image=bg_search1)
search1_label.place(x=0, y=0, relwidth=1, relheight=1)

search_backbutton = Button(frame24, padx=40, pady=20, bg="black", command= lambda: show_frame(search))
search_backbutton.place(x=10, y=10)

"==================================================FRAME 2(ISSUE)=========================================================================================================================="

bg_issue = PhotoImage(file="Images/Illustration21.png")
issue_label = Label(issue, image=bg_issue)
issue_label.place(x=0, y=0, relwidth=1, relheight=1)
def issuef():
   def issuecheck():
      member=comMember.get()
      admissionno = txtadmission_no.get()
      bookcode = txtbook_code1.get()
      if not admissionno or not bookcode:
         Label(issue, text="Arey kuch type toh karo", font=('Century 15 bold')).pack(pady=20)
      elif check_admission_no(admissionno)==0:
         Label(issue, text="Admission number not found in database", font=('Century 15 bold')).pack(pady=20)
      elif check_book_code(bookcode)==0:
         Label(issue, text="Invalid Book Code", font=('Century 15 bold')).pack(pady=20)
      else:
         show_frame(frame9)
         yy=book_availability(admissionno,bookcode)
         booktitle="Title : "+yy[4]
         bookauthor="Author : "+str(yy[5])
         childname="Student Name : "+yy[1]
         childclass="Class : "+str(yy[2])+yy[3]

         title = Label(txtBox, width=41, text=booktitle, padx=-10, pady=0)
         title.grid(row=0, column=0)

         Author = Label(txtBox, width=41, text=bookauthor, padx=-10, pady=10)
         Author.grid(row=1, column=0)

         name = Label(txtBox,  width=41, text=childname, padx=-10, pady=15)
         name.grid(row=2, column=0)

         classes = Label(txtBox, width=41, text=childclass, padx=-10, pady=20)
         classes.grid(row=3,column=0)

         if yy[0]=="no copy":
            booknot_found = Label(txtBox, width=21, text="No copies of the book available at the moment.", padx=-10, pady=0)
            booknot_found.grid(row=4, column=0)
            email_message = Label(txtBox, width=21, text="Would you like to receive an email when the book will be available", padx=-10, pady=0)
            email_message.grid(row=5, column=0)
            email_button = Button(issue_confirm, text="SEND EMAIL", fg='white', padx=220, pady=20, borderwidth=3, bg="#1E1E20", command=lambda: [availability_email(admissionno, bookcode), show_frame(issue_confirmation)] )
            email_button.place(x=0, y=275)
            frame3_title = tk.Label(issue_confirmation, text='An Email will be sent to you when the book is available.', bg='black', fg="white", font='times 35')
            frame3_title.place(x=780, y=450)
         else:
            confirm_button = Button(issue_confirm, text="CONFIRM", fg='white', padx=220, pady=20, borderwidth=3, bg="#1E1E20", command=lambda: [issue_book(admissionno,bookcode),show_frame(issue_confirmation)])
            confirm_button.place(x=0, y=275)
            frame3_title = tk.Label(issue_confirmation, text='BOOK ISSUED!', bg='black', fg="white", font='times 35')
            frame3_title.place(x=780, y=450)

      #Label(issue, text=member, font= ('Century 15 bold')).pack(pady=20)
      #Label(issue, text=admissionno, font=('Century 15 bold')).pack(pady=40)
      #Label(issue, text=bookcode, font=('Century 15 bold')).pack(pady=20)

   issueframe=LabelFrame(issue, text="ISSUE DETAILS", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
   issueframe.place(x=600, y=250, width=700, height=500)

   lblmember=Label(issueframe, bg="#C1C1C1", text="Member", font=("times new roman", 28, "bold"), padx=140, pady=0)
   lblmember.grid(row=1, column=0, sticky=W)

   comMember=ttk.Combobox(issueframe, font=("ariel", 20), width=11, state="readonly")
   comMember["value"]=("Admin","Staff", "Student")
   comMember.grid(row=1, column=1)

   lbladmission_no = Label(issueframe, bg="#C1C1C1", text="Admission Number", font=("times new roman", 28, "bold"), padx=55, pady=0)
   lbladmission_no.grid(row=2, column=0, sticky=W)

   txtadmission_no=Entry(issueframe, font=("times new roman", 20, "bold"), width= 13)
   txtadmission_no.grid(row=2, column=1)

   lblbook_code = Label(issueframe, bg="#C1C1C1", text="Book Code", font=("times new roman", 28, "bold"), padx=121, pady=0)
   lblbook_code.grid(row=3, column=0, sticky=W)

   txtbook_code1 = Entry(issueframe, font=("times new roman", 20, "bold"), width=13)
   txtbook_code1.grid(row=3, column=1)

   next_button = Button(issueframe, text="NEXT", fg="white", padx=85, pady=10, borderwidth=3, bg="#1E1E20", command= lambda : issuecheck())
   next_button.grid(row=4, column=1)

   #click_btn= PhotoImage(file= r'Images\button4.png')
   #img_label= Label(image=click_btn)

   issue_backbutton = Button(issue, padx=40, pady=20, bg="black", command= lambda: show_frame(mainframe))
   issue_backbutton.place(x=10, y=10)
   show_frame(issue)

"==================================================FRAME 9(DETAILS CONFIRMATION OF ISSUED BOOK)=========================================================================================================================="
bg_issue2 = PhotoImage(file="Images/Illustration21.png")
issue2_label=Label(frame9, image=bg_issue2)
issue2_label.place(x=0, y=0, relwidth=1, relheight=1)

#def issuebook()


#def whatever code you wrote for issuing book...

issue_confirm = LabelFrame(frame9, text="CONFIRMATION", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
issue_confirm.place(x=650, y=250, width=560, height=500)

txtBox=Text(issue_confirm, font=("arial", 15, "bold"), width=60, height=7, padx=149, pady=50)
txtBox.grid(row=0, column=0, columnspan=4)

confirm_button=Button(issue_confirm, text="CONFIRM", fg='white', padx=220, pady=20, borderwidth=3, bg="#1E1E20", command=lambda: show_frame(issue_confirmation))
confirm_button.place(x=0, y=275)

frame9_backbutton = Button(frame9, padx=40, pady=20, bg="black", command= lambda: show_frame(issue))
frame9_backbutton.place(x=10, y=10)

"==================================================FRAME 3(CONFIRMATION OF ISSUED BOOK)=========================================================================================================================="
bg_issue3 = PhotoImage(file="Images/Illustration21.png")
issue3_label=Label(issue_confirmation, image=bg_issue3)
issue3_label.place(x=0, y=0, relwidth=1, relheight=1)

#TODO : ADD A TXT BOX FOR DETAILS
#
'''issue_confirm = LabelFrame(frame9, text="CONFIRMATION", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
issue_confirm.place(x=650, y=250, width=560, height=500)

txtBox=Text(issue_confirm, font=("arial", 15, "bold"), width=60, height=7, padx=149, pady=50)
txtBox.grid(row=0, column=0, columnspan=4)

confirm_button=Button(issue_confirm, text="CONFIRM", fg='white', padx=220, pady=20, borderwidth=3, bg="#1E1E20", command=lambda: show_frame(issue_confirmation))
confirm_button.place(x=0, y=275)

frame9_backbutton = Button(frame9, padx=40, pady=20, bg="black", command= lambda: show_frame(issue))
frame9_backbutton.place(x=10, y=10)'''

frame3_btn = tk.Button(issue_confirmation, text='RETURN TO HOME PAGE', command=lambda: show_frame(mainframe), bg="#1E1E20", fg= 'white', padx=100, pady=15)
frame3_btn.place(x=770, y=550)

bg_return = PhotoImage(file="Images/Illustration6.png")
return_label=Label(frame5, image=bg_return)
return_label.place(x=0, y=0, relwidth=1, relheight=1)
"==================================================FRAME 5(RETURN BOOK)=========================================================================================================================="
bg_return1 = PhotoImage(file="Images/Illustration21.png")
return1_label=Label(frame5, image=bg_return1)
return1_label.place(x=0, y=0, relwidth=1, relheight=1)

def returnf():
   def returncheck():
      recordno=txtrecord_no.get()
      if not recordno:
         Label(frame5, text="Arey kuch toh type kar", font= ('Century 15 bold')).pack(pady=20)
      elif record_no_check(recordno)==0:
         Label(frame5, text="Record not Found", font=('Century 15 bold')).pack(pady=20)
      else:
         return_student=show_child()
         returned_book=show_book()
         fine=fine_check()
         if fine==0:
            fine = "You have returned the book on time, you do not have to pay the fine"
         else:
            fine = "Due to late submission you have to pay a fine of Rs." + str(fine)
         returnbookname=returned_book[0]
         returnbookauthor=returned_book[1]
         returnstudentname=return_student[0]
         returnstudentclass=str(return_student[1])+return_student[2]

         title = Label(txtBoxreturn, width=21, text=returnbookname, padx=-10, pady=-10)
         title.grid(row=0, column=0)

         Author = Label(txtBoxreturn, width=21, text=returnbookauthor, padx=-10, pady=10)
         Author.grid(row=1, column=0)

         name = Label(txtBoxreturn, width=21, text=returnstudentname, padx=-10, pady=15)
         name.grid(row=2, column=0)

         classes = Label(txtBoxreturn, width=21, text=returnstudentclass, padx=-10, pady=20)
         classes.grid(row=3, column=0)

         fine = Label(txtBoxreturn, width=21, text=fine, padx=-10, pady=22)
         fine.grid(row=4, column=0)
         show_frame(frame10)
         confirm_button = Button(return_confirm, text="CONFIRM", fg='white', padx=220, pady=20, borderwidth=3, bg="#1E1E20", command=lambda: [return_book(),send_email(),show_frame(frame11)])
         confirm_button.place(x=0, y=275)

   returnframe=LabelFrame(frame5, text="RETURN DETAILS", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
   returnframe.place(x=600, y=250, width=700, height=500)

   lblrecord_no=Label(returnframe, bg="#C1C1C1", text="Record Number", font=("times new roman", 28, "bold"), padx=94, pady=0)
   lblrecord_no.grid(row=1, column=0, sticky=W)

   txtrecord_no=Entry(returnframe, font=("times new roman", 20, "bold"), width= 13)
   txtrecord_no.grid(row=1, column=1)

   next_button = Button(returnframe, text="NEXT", fg="white", padx=85, pady=10, borderwidth=3, bg="#1E1E20", command= lambda : returncheck())
   next_button.grid(row=3, column=1)

   return_backbutton = Button(frame5, padx=40, pady=20, bg="black", command= lambda: show_frame(mainframe))
   return_backbutton.place(x=10, y=10)
   show_frame(frame5)
'==================================================FRAME 10(RETURN BOOK DETAILS CONFIRMATION)=========================================================================================================================='
bg_return2 = PhotoImage(file="Images/Illustration21.png")
return2_label=Label(frame10, image=bg_return2)
return2_label.place(x=0, y=0, relwidth=1, relheight=1)

#Whatever code you wrote to return book...

return_confirm = LabelFrame(frame10, text="CONFIRMATION", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
return_confirm.place(x=650, y=250, width=560, height=500)

txtBoxreturn=Text(return_confirm, font=("arial", 15, "bold"), width=18, height=7, padx=149, pady=50)
txtBoxreturn.grid(row=0, column=0, columnspan=2)

frame10_backbutton = Button(frame10, padx=40, pady=20, bg="black", command= lambda: show_frame(frame5))
frame10_backbutton.place(x=10, y=10)

'==================================================FRAME 11(RETURN BOOK CONFIRMATION)=========================================================================================================================='
bg_return3 = PhotoImage(file="Images/Illustration21.png")
return3_label=Label(frame11, image=bg_return3)
return3_label.place(x=0, y=0, relwidth=1, relheight=1)

frame11_title = tk.Label(frame11, text='BOOK RETURNED!', bg= 'black', fg= "white", font='times 35')
frame11_title.place(x=745, y=450)

frame11_btn = tk.Button(frame11, text='RETURN TO HOME PAGE', command=lambda: show_frame(mainframe), bg="#1E1E20", fg= 'white', padx=100, pady=15)
frame11_btn.place(x=770, y=550)

'==================================================FRAME 6(EXTENTION)=========================================================================================================================='

bg_extention1 = PhotoImage(file="Images/Illustration21.png")
extention1_label=Label(frame6, image=bg_extention1)
extention1_label.place(x=0, y=0, relwidth=1, relheight=1)

def extentionf():
   def extension():
      recordnu= txtrecord_number.get()
      if not recordnu:
         Label(frame6, text="Arey kuch toh type kar", font=('Century 15 bold')).pack(pady=20)
      elif record_no_check(recordnu) == 0:
         Label(frame6, text="Record not Found", font=('Century 15 bold')).pack(pady=20)
      else:
         extend_student = show_child()
         extend_book = show_book()
         extend_fine = fine_check()
         extendbookname = extend_book[0]
         extendbookauthor = extend_book[1]
         extendstudentname = extend_student[0]
         extendstudentclass = str(extend_student[1]) + extend_student[2]

         title = Label(txtBoxextention, width=21, text=extendbookname, padx=-10, pady=-10)
         title.grid(row=0, column=0)

         Author = Label(txtBoxextention, width=21, text=extendbookauthor, padx=-10, pady=10)
         Author.grid(row=1, column=0)

         name = Label(txtBoxextention, width=21, text=extendstudentname, padx=-10, pady=15)
         name.grid(row=2, column=0)

         classes = Label(txtBoxextention, width=21, text=extendstudentclass, padx=-10, pady=20)
         classes.grid(row=3, column=0)

         if extend_fine==0:
            pass
         else:
            extend_fine = "Due to late submission you have to pay a fine of Rs." + str(fine)
            fine = Label(txtBoxextention, width=21, text=extend_fine, padx=-10, pady=22)
            fine.grid(row=4, column=0)
         confirm_button = Button(extention_confirm, text="CONFIRM", fg='white', padx=220, pady=20, borderwidth=3,
                                 bg="#1E1E20", command=lambda: [extend(recordnu),extend_email(recordnu), show_frame(frame13)])
         confirm_button.place(x=0, y=275)
         show_frame(frame12)

      #Label(frame6, text=recordnu, font= ('Century 15 bold')).pack(pady=20)

   extentionframe=LabelFrame(frame6, text="EXTENTION DETAILS", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
   extentionframe.place(x=600, y=250, width=700, height=500)

   lblrecord_no=Label(extentionframe, bg="#C1C1C1", text="Record Number", font=("times new roman", 28, "bold"), padx=94, pady=0)
   lblrecord_no.grid(row=1, column=0, sticky=W)

   txtrecord_number= Entry(extentionframe, font=("times new roman", 20, "bold"), width= 13)
   txtrecord_number.grid(row=1, column=1)

   next_button = Button(extentionframe, text="NEXT", fg="white", padx=85, pady=10, borderwidth=3, bg="#1E1E20", command= lambda : extension())
   next_button.grid(row=3, column=1)

   extention_backbutton = Button(frame6, padx=40, pady=20, bg="black", command= lambda: show_frame(mainframe))
   extention_backbutton.place(x=10, y=10)
   show_frame(frame6)
'==================================================FRAME 12(EXTENTION DETAILS CONFIRMATION)=========================================================================================================================='
bg_extention2 = PhotoImage(file="Images/Illustration21.png")
extention2_label=Label(frame12, image=bg_extention2)
extention2_label.place(x=0, y=0, relwidth=1, relheight=1)

#Whatever code you wrote for extention...

extention_confirm = LabelFrame(frame12, text="CONFIRMATION", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
extention_confirm.place(x=650, y=250, width=560, height=500)

txtBoxextention=Text(extention_confirm, font=("arial", 15, "bold"), width=18, height=7, padx=149, pady=50)
txtBoxextention.grid(row=0, column=0, columnspan=2)

frame12_backbutton = Button(frame12, padx=40, pady=20, bg="black", command= lambda: show_frame(frame6))
frame12_backbutton.place(x=10, y=10)

'==================================================FRAME 13(EXTENTION BOOK CONFIRMATION)=========================================================================================================================='
bg_extention3 = PhotoImage(file="Images/Illustration21.png")
extention3_label=Label(frame13, image=bg_extention3)
extention3_label.place(x=0, y=0, relwidth=1, relheight=1)

frame13_title = tk.Label(frame13, text='EXTENSION GRANTED!', fg= "white", bg= 'black', font='times 35')
frame13_title.place(x=750, y=450)

frame13_btn = tk.Button(frame13, text='RETURN TO HOME PAGE', command=lambda: show_frame(mainframe), bg="#1E1E20", fg= 'white', padx=100, pady=15)
frame13_btn.place(x=770, y=550)

"==================================================FRAME 7(ISSUE RECORDS)=========================================================================================================================="
bg_record = PhotoImage(file="Images/Illustration21.png")
records_label = Label(frame7, image=bg_record)
records_label.place(x=0, y=0, relwidth=1, relheight=1)

issue_record = LabelFrame(frame7, text="ISSUE RECORDS", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
issue_record.place(x=450, y=250, width=900, height=500)

issue_no= Label(frame7, width=85, text= "RECORD NO.              ADM NO.           BOOK CODE     ISSUE DATE       REUTRN DATE          FINAL RD         STATUS", font=("ariel", 12, "bold"))
issue_no.place(x=474, y=280)

txtBox_issuerecord=Text(issue_record, font=("arial", 15, "bold"), width=20, height=7, padx=160, pady=50)
txtBox_issuerecord.grid(row=0, column=0, columnspan=2)

"""ii = show_all_records()
i=0

for tiger in ii:
   #print (tiger)
   for j in range (len(tiger)):
      e = Label(txtBox_issuerecord, width=13, text=tiger[j])
      e.grid(row=i, column=j)
   i+=1"""

ir_backbutton = Button(frame7, padx=40, pady=20, bg="black", command= lambda: show_frame(mainframe))
ir_backbutton.place(x=10, y=10)

"==================================================FRAME 8(STOCK)=========================================================================================================================="
bg_stock = PhotoImage(file="Images/Illustration21.png")
stock_label=Label(frame8, image=bg_stock)
stock_label.place(x=0, y=0, relwidth=1, relheight=1)

frame8_show = tk.Button(frame8, text='SHOW BOOKS', fg='white', command=lambda: show_frame(frame14), bg="#1E1E20", padx=200, pady=20)
frame8_show.place(x=150, y=600)

frame8_add = tk.Button(frame8, text='ADD BOOKS',fg='white', command=lambda: show_frame(frame15), bg="#1E1E20", padx=200, pady=20)
frame8_add.place(x=738, y=600)

frame8_update = tk.Button(frame8, text='UPDATE BOOKS',fg='white', command=lambda: show_frame(frame16), bg="#1E1E20", padx=200, pady=20)
frame8_update.place(x=1300, y=600)

frame8_delete = tk.Button(frame8, text='DELETE BOOKS',fg='white', command=lambda: show_frame(frame17), bg="#1E1E20", padx=200, pady=20)
frame8_delete.place(x=440, y=690)

frame8_studentlist = tk.Button(frame8, text='STUDENT LIST',fg='white', command=lambda: [all_students(), show_frame(frame18)], bg="#1E1E20", padx=200, pady=20)
frame8_studentlist.place(x=1020, y=690)

frame8_backbutton = Button(frame8, padx=40, pady=20, bg="black", command= lambda: show_frame(mainframe))
frame8_backbutton.place(x=10, y=10)

"==================================================FRAME 14(SHOW BOOKS)=========================================================================================================================="
bg_booklist = PhotoImage(file="Images/Illustration21.png")
booklist_label=Label(frame14, image=bg_booklist)
booklist_label.place(x=0, y=0, relwidth=1, relheight=1)

book_list = LabelFrame(frame14, padx=20, bg="#444444")
book_list.place(x=595, y=350, width=735, height=500)

scrollbar = Scrollbar(book_list, orient= VERTICAL)
scrollbar.pack(side = RIGHT, fill= Y)

txtBox_booklist = Text(book_list, font=(15), width=100, height=5, padx=0, pady=0)
txtBox_booklist.pack(side= LEFT , fill = BOTH)

txtBox_booklist.config(yscrollcommand= scrollbar.set)
scrollbar.config(command = txtBox_booklist.yview)

Seriel_no= Label(frame14, width=81, text= "No.              NAME           AUTHOR     PUBLICATION       ISBN          QUANTITY         TAG", font=("bold"))
Seriel_no.place(x=595, y=329)

'''for line in range(100):
   txtBox_booklist.insert(END, "this is line number" + str(line))'''

ii = show_all_books()
i=0

for tiger in ii:
   #print (tiger)
   for j in range (len(tiger)):
      e = Label(txtBox_booklist, width=13, text=tiger[j])
      e.grid(row=i, column=j)
   i+=1
   #txtBox_booklist.insert(END, i)

frame14_backbutton = Button(frame14, padx=40, pady=20, bg="black", command= lambda: show_frame(frame8))
frame14_backbutton.place(x=10, y=10)

"==================================================FRAME 15(ADD BOOKS)=========================================================================================================================="
def get_value():
   bookname=txtbookname.get()
   authorname = txtauthor.get()
   publicationname = txtpublication.get()
   ISBN = txtISBN.get()
   bookquantity = txtquantity.get()
   booktags = txttags.get()

   addbooks(bookname,authorname,publicationname,ISBN,bookquantity,booktags)
   #Label(frame15, text=bookname, font= ('Century 15 bold')).pack(pady=20)
   #Label(frame15, text=authorname, font=('Century 15 bold')).pack(pady=40)
   #Label(frame15, text=publicationname, font=('Century 15 bold')).pack(pady=60)
   #Label(frame15, text=ISBN, font=('Century 15 bold')).pack(pady=80)
   #Label(frame15, text=bookquantity, font= ('Century 15 bold')).pack(pady=100)
   #Label(frame15, text=booktags, font= ('Century 15 bold')).pack(pady=120)

bg_addbook = PhotoImage(file="Images/Illustration21.png")
addbook_label=Label(frame15, image=bg_addbook)
addbook_label.place(x=0, y=0, relwidth=1, relheight=1)

addframe=LabelFrame(frame15, text="ADD BOOK", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
addframe.place(x=600, y=250, width=700, height=500)

lblbookname = Label(addframe, bg="#C1C1C1", text="Book Name", font=("times new roman", 28, "bold"), padx=126, pady=0)
lblbookname.grid(row=0, column=0, sticky=W)

txtbookname=Entry(addframe, font=("times new roman", 20, "bold"), width= 13)
txtbookname.grid(row=0, column=1)

lblauthor = Label(addframe, bg="#C1C1C1", text="Author", font=("times new roman", 28, "bold"), padx=159, pady=0)
lblauthor.grid(row=1, column=0, sticky=W)

txtauthor = Entry(addframe, font=("times new roman", 20, "bold"), width=13)
txtauthor.grid(row=1, column=1)

lblpublication = Label(addframe, bg="#C1C1C1", text="Publication:", font=("times new roman", 28, "bold"), padx=120, pady=0)
lblpublication.grid(row=2, column=0, sticky=W)

txtpublication=Entry(addframe, font=("times new roman", 20, "bold"), width= 13)
txtpublication.grid(row=2, column=1)

lblISBN = Label(addframe, bg="#C1C1C1", text="ISBN No.", font=("times new roman", 28, "bold"), padx=142, pady=0)
lblISBN.grid(row=3, column=0, sticky=W)

txtISBN = Entry(addframe, font=("times new roman", 20, "bold"), width=13)
txtISBN.grid(row=3, column=1)

lblquantity = Label(addframe, bg="#C1C1C1", text="Quantity", font=("times new roman", 28, "bold"), padx=145, pady=0)
lblquantity.grid(row=4, column=0, sticky=W)

txtquantity =Entry(addframe, font=("times new roman", 20, "bold"), width= 13)
txtquantity.grid(row=4, column=1)

lbltags = Label(addframe, bg="#C1C1C1", text="Tags", font=("times new roman", 28, "bold"), padx=178, pady=0)
lbltags.grid(row=5, column=0, sticky=W)

txttags = Entry(addframe, font=("times new roman", 20, "bold"), width=13)
txttags.grid(row=5, column=1)

add_button = Button(addframe, text="ADD", fg="white", padx=85, pady=10, borderwidth=3, bg="#1E1E20", command= lambda : [get_value(), show_frame(frame19)])
add_button.grid(row=6, column=1)

frame15_backbutton = Button(frame15, padx=40, pady=20, bg="black", command= lambda:show_frame(frame8))
frame15_backbutton.place(x=10, y=10)

"==================================================FRAME 19(BOOK ADDITION CONFIRMATION)=========================================================================================================================="
bg_addbook1 = PhotoImage(file="Images/Illustration21.png")
addbook1_label=Label(frame19, image=bg_addbook1)
addbook1_label.place(x=0, y=0, relwidth=1, relheight=1)

frame19_title = tk.Label(frame19, text='BOOK ADDED!', bg= "black", fg="white", font='times 35')
frame19_title.place(x=775, y=450)

frame19_btn = tk.Button(frame19, text='RETURN TO HOME PAGE', command=lambda: show_frame(mainframe), bg="#1E1E20", fg= 'white', padx=100, pady=15)
frame19_btn.place(x=770, y=550)

"==================================================FRAME 18(STUDENT LIST)=========================================================================================================================="
bg_studentlist = PhotoImage(file="Images/Illustration21.png")
studentlist_label=Label(frame18, image=bg_studentlist)
studentlist_label.place(x=0, y=0, relwidth=1, relheight=1)

def all_students():
   ii = show_students()
   i=0
   for tiger in ii:
      #print (tiger)
      for j in range (len(tiger)):
         e = Label(txtBox_studentlist, width=13, text=tiger[j])
         e.grid(row=i, column=j)
      i+=1

student_list = LabelFrame(frame18, text="STUDENT LIST", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
student_list.place(x=650, y=250, width=560, height=500)

txtBox_studentlist=Text(student_list, font=("arial", 15, "bold"), width=18, height=7, padx=149, pady=130, state= "disabled")
txtBox_studentlist.grid(row=0, column=0, columnspan=2)

sl_backbutton = Button(frame18, padx=40, pady=20, bg="black", command= lambda: show_frame(frame8))
sl_backbutton.place(x=10, y=10)

"==================================================FRAME 16(UPDATE BOOK)=========================================================================================================================="
bg_updatebook = PhotoImage(file="Images/Illustration21.png")
updatebook_label=Label(frame16, image=bg_updatebook)
updatebook_label.place(x=0, y=0, relwidth=1, relheight=1)

def update_value():
   bookcode = txtbook_code.get()
   if not bookcode:
      Label(frame16, text="Arey kuch toh type karo", font=('Century 15 bold')).pack(pady=200)
   else:
      abcd=book_code_check(bookcode)
      if not abcd:
         Label(frame16, text="No such book Code exist", font=('Century 15 bold')).pack(pady=200)
      else:
         novel_name="Name of the Book : "+abcd[1]
         novel_author="Author of the Book : "+abcd[2]
         novel_publisher="Publisher of the Book : "+str(abcd[3])
         novel_ISBN="ISBN Number : "+str(abcd[4])
         novel_quantity="Quantity of the Book : "+str(abcd[5])
         novel_tags="Tags : "+str(abcd[6])

         name_book = Label(txtBox_update, width=20, text=novel_name)
         name_book.grid(row=0, column=0)
         name_author = Label(txtBox_update, width=20, text=novel_author)
         name_author.grid(row=1, column=0)
         publisher = Label(txtBox_update, width=20, text=novel_publisher)
         publisher.grid(row=2, column=0)
         ISBN = Label(txtBox_update, width=20, text=novel_ISBN)
         ISBN.grid(row=3,column=0)
         Quantity = Label(txtBox_update, width=20, text=novel_quantity)
         Quantity.grid(row=4,column=0)
         Tags = Label(txtBox_update, width=20, text=novel_tags)
         Tags.grid(row=5,column=0)
         show_frame(frame20)
         def final_update():
            Book_data = combookdata.get()
            update_data = txtenterdata_no.get()
            if not Book_data or not update_data:
               Label(frame20, text="Arey kuch toh enter karo", font=('Century 15 bold')).pack(pady=200)
            else:
               if Book_data=="Name":
                  update_book_name(update_data,bookcode)
               elif Book_data == "Author":
                  update_author_name(update_data, bookcode)
               elif Book_data == "Publication":
                  update_publication_name(update_data, bookcode)
               elif Book_data == "ISBN":
                  update_ISBN_number(update_data, bookcode)
               elif Book_data == "Quantity":
                  update_quantity_of_book(update_data, bookcode)
               elif Book_data == "Tags":
                  update_book_tag(update_data, bookcode)
               show_frame(frame21)
         next_button = Button(updateframe, text="NEXT", fg="white", padx=85, pady=10, borderwidth=3, bg="#1E1E20",
                              command=lambda: final_update())
         next_button.place(x=315, y=343)

updateframe=LabelFrame(frame16, text="UPDATE BOOK", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
updateframe.place(x=600, y=250, width=700, height=500)

lblbook_code=Label(updateframe, bg="#C1C1C1", text="Book Code", font=("times new roman", 28, "bold"), padx=94, pady=0)
lblbook_code.grid(row=1, column=0, sticky=W)

txtbook_code=Entry(updateframe, font=("times new roman", 20, "bold"), width= 13)
txtbook_code.grid(row=1, column=1)

next_button = Button(updateframe, text="NEXT", fg="white", padx=85, pady=10, borderwidth=3, bg="#1E1E20", command= lambda : [update_value()])
next_button.grid(row=3, column=1)

update_backbutton = Button(frame16, padx=40, pady=20, bg="black", command= lambda: show_frame(frame8))
update_backbutton.place(x=10, y=10)


"==================================================FRAME 20(UPDATE BOOK DATA)=========================================================================================================================="
bg_updatebook1 = PhotoImage(file="Images/Illustration21.png")
updatebook1_label=Label(frame20, image=bg_updatebook1)
updatebook1_label.place(x=0, y=0, relwidth=1, relheight=1)

updateframe = LabelFrame(frame20, text="UPADTE BOOK", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
updateframe.place(x=690, y=250, width=570, height=500)

txtBox_update = Text(updateframe, font=("arial", 15, "bold"), width=18, height=7, padx=149, pady=30)
txtBox_update.place(x=10, y=10)

lbldata = Label(updateframe, bg="#C1C1C1", text="Data", font=("times new roman", 24, "bold"), padx=117, pady=0)
lbldata.place(x=10, y=250)

comBookdata = tk.StringVar()
combookdata = ttk.Combobox(updateframe, font=("ariel", 20), width=11, state="readonly")
combookdata["value"] = ("Name", "Author", "Publication", "ISBN", "Quantity", "Tags")
combookdata.place(x=324, y=251)

lblenterdata = Label(updateframe, bg="#C1C1C1", text="Enter Data", font=("times new roman", 24, "bold"),padx=75, pady=0)
lblenterdata.place(x=10, y=300)

txtenterdata_no = Entry(updateframe, font=("times new roman", 20, "bold"), width=13)
txtenterdata_no.place(x=324, y=300)



frame20_backbutton = Button(frame20, padx=40, pady=20, bg="black", command=lambda: show_frame(frame16))
frame20_backbutton.place(x=10, y=10)




def updatevalue():

   #if not Book_data or not update_date:
   #   Label(frame20, text="Arey kuch toh enter karo", font=('Century 15 bold')).pack(pady=200)
   #elif

   try:
      if Book_data=="":
         Label(frame20, text="Arey kuch toh type karo", font=('Century 15 bold')).pack(pady=200)
      else:
         if Book_data=="Name":
            update_book_name(update_data,update_book_code)
         elif Book_data=="Author":
            update_author_name(update_data,update_book_code)
         elif Book_data=="Publication":
            update_publication_name(update_data,update_book_code)
         elif Book_data == "ISBN":
            update_ISBN_number(update_data,update_book_code)
         elif Book_data == "Quantity":
            update_quantity_of_book(update_data,update_book_code)
         elif Book_data == "Tags":
            update_book_tag(update_data,update_book_code)
         show_frame(frame21)
   except:
      Label(frame20, text="ERROR IN DATA", font=('Century 15 bold')).pack(pady=200)


"==================================================FRAME 21(BOOK UPDATE CONFIRMATION)=========================================================================================================================="
bg_updatebook2 = PhotoImage(file="Images/Illustration21.png")
updatebook2_label=Label(frame21, image=bg_updatebook2)
updatebook2_label.place(x=0, y=0, relwidth=1, relheight=1)

frame21_title = tk.Label(frame21, text='BOOK UPDATED!', bg= "black", fg="white", font='times 35')
frame21_title.place(x=750, y=450)

frame21_btn = tk.Button(frame21, text='RETURN TO HOME PAGE', command=lambda: show_frame(mainframe), bg="#1E1E20", fg= 'white', padx=100, pady=15)
frame21_btn.place(x=770, y=550)

"==================================================FRAME 17(DELETE BOOK)=========================================================================================================================="
bg_deletebook = PhotoImage(file="Images/Illustration21.png")
deletebook_label=Label(frame17, image=bg_deletebook)
deletebook_label.place(x=0, y=0, relwidth=1, relheight=1)

def deletebook():
   bookcode=txtbookcode.get()
   if not bookcode:
      Label(frame16, text="Arey kuch toh type karo", font=('Century 15 bold')).pack(pady=200)
   else:
      abcd = book_code_check(bookcode)
      if not abcd:
         Label(frame16, text="No such book Code exist", font=('Century 15 bold')).pack(pady=200)
      else:
         novel_name = "Name of the Book : " + abcd[1]
         novel_author = "Author of the Book : " + str(abcd[2])
         novel_publisher = "Publisher of the Book : " + str(abcd[3])
         novel_ISBN = "ISBN Number : " + str(abcd[4])
         novel_quantity = "Quantity of the Book : " + str(abcd[5])
         novel_tags = "Tags : " + str(abcd[6])

         name_book = Label(txtBox_delete, width=20, text=novel_name)
         name_book.grid(row=0, column=0)
         name_author = Label(txtBox_delete, width=20, text=novel_author)
         name_author.grid(row=1, column=0)
         publisher = Label(txtBox_delete, width=20, text=novel_publisher)
         publisher.grid(row=2, column=0)
         ISBN = Label(txtBox_delete, width=20, text=novel_ISBN)
         ISBN.grid(row=3, column=0)
         Quantity = Label(txtBox_delete, width=20, text=novel_quantity)
         Quantity.grid(row=4, column=0)
         Tags = Label(txtBox_delete, width=20, text=novel_tags)
         Tags.grid(row=5, column=0)
         show_frame(frame22)
         delete_button = Button(delete_frame, text="DELETE", fg="white", padx=85, pady=10, borderwidth=3, bg="#1E1E20", command=lambda: [delete_book(bookcode),show_frame(frame23)])
         delete_button.place(x=295, y=343)

deleteframe=LabelFrame(frame17, text="DELETE BOOK", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
deleteframe.place(x=650, y=250, width=627, height=500)

lblbook_code=Label(deleteframe, bg="#C1C1C1", text="Book Code", font=("times new roman", 28, "bold"), padx=94, pady=0)
lblbook_code.grid(row=1, column=0, sticky=W)

txtbookcode=Entry(deleteframe, font=("times new roman", 20, "bold"), width= 13)
txtbookcode.grid(row=1, column=1)

next_button = Button(deleteframe, text="NEXT", fg="white", padx=85, pady=10, borderwidth=3, bg="#1E1E20", command= lambda : deletebook())
next_button.grid(row=3, column=1)

delete_backbutton = Button(frame17, padx=40, pady=20, bg="black", command= lambda: show_frame(frame8))
delete_backbutton.place(x=10, y=10)

"==================================================FRAME 22(DELETE BOOK DATA)=========================================================================================================================="
bg_deletebook1 = PhotoImage(file="Images/Illustration21.png")
deletebook1_label=Label(frame22, image=bg_deletebook1)
deletebook1_label.place(x=0, y=0, relwidth=1, relheight=1)

#def delete_or_not():
#whatever delete function you wrote?...

delete_frame=LabelFrame(frame22, text="DELETE BOOK", bd=5, relief=RAISED, font=("arial italic", 20), padx=20, bg="#DCDCDC")
delete_frame.place(x=690, y=250, width=570, height=500)

txtBox_delete=Text(delete_frame, font=("arial", 15, "bold"), width=18, height=7, padx=149, pady=50)
txtBox_delete.place(x=10, y=10)



frame22_backbutton = Button(frame22, padx=40, pady=20, bg="black", command= lambda: show_frame(frame17))
frame22_backbutton.place(x=10, y=10)

"==================================================FRAME 23(DELETE CONFIRMATION)=========================================================================================================================="
bg_deletebook2 = PhotoImage(file="Images/Illustration21.png")
deletebook2_label=Label(frame23, image=bg_deletebook2)
deletebook2_label.place(x=0, y=0, relwidth=1, relheight=1)

frame23_title = tk.Label(frame23, text='BOOK DELETED!', bg= "black", fg="white", font='times 35')
frame23_title.place(x=750, y=450)

frame23_btn = tk.Button(frame23, text='RETURN TO HOME PAGE', command=lambda: show_frame(mainframe), bg="#1E1E20", fg= 'white', padx=100, pady=15)
frame23_btn.place(x=770, y=550)

warning_email_send()
show_frame(mainframe)

window.mainloop()