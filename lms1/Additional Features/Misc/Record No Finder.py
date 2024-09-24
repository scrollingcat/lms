def record_no_finder(admission_no):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='lms')
    cur_lms = lms.cursor()
    command28="select * from issue_records where admission_no="+admission_no+" and return_status=0"
    cur_lms.execute(command28)
    issued_book_record=cur_lms.fetchall()
    if not  issued_book_record:
        print("NO Records found for the admission no")
    else:
        details=sql.connect(host='localhost', user='root', password='tiger', database='details')
        cur_details=details.cursor()
        command62="select name,class,section from students where admission_no="+admission_no
        cur_details.execute(command62)
        kid=cur_details.fetchone()
        print("Name of Student :",kid[0])
        print("Class and Section :",kid[1],kid[2])
        result_no=1
        for k in issued_book_record:
            command61 = "select name_of_book from books where book_code="+str(k[2])
            cur_lms.execute(command61)
            bookname=cur_lms.fetchone()
            bookname=bookname[0]
            print("Result",result_no)
            print("Name of book :",bookname)
            print("Record Number :",k[0])
            print("Issue Date :",k[3])
            print("Return Date :",k[4])
            result_no+=1
a=input("enter your admission no")
record_no_finder(a)