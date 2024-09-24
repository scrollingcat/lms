try:
    import mysql.connector as sql
    mydb=sql.connect(host='localhost', user='root' ,password='tiger')
    cur=mydb.cursor()
    cur.execute("create database LMS")
    cur.execute("use lms")
    cur.execute("create table Books (Book_Code int(4) Primary key auto_increment,\
                Name_of_Book varchar(75) not null, Author varchar(50), Publisher varchar(50),\
                ISBN varchar(13), Quantity int(2) default 1, Tags varchar(10))")
    cur.execute("create table Issue_Records(Record_No int primary key auto_increment,\
                Admission_No int(6) not null, Book_Code int(4) not null, Issue_Date date not null,\
                Return_Date date not null, Final_Return_Date date, Return_Status bit(1) default 0)")
    cur.execute("Create database Details")
    cur.execute("use details")
    cur.execute("Create Table Students(Admission_No int(6) primary key, Name varchar(25) not null, Class int(2) not null, Section varchar(1) not null, Phone_No varchar(10), Email varchar(50))")
    cur.execute("create database email")
    cur.execute("use email")
    cur.execute("create table availability(serial_no int primary key auto_increment, admission_no int not null, required_book_code int, email_status bit(1) default 0)")
    print("All databases and Tables have been successfully created, you're ready to go!")
except:
    print("One of the following databases exists,kindly delete them: \n1.LMS\n2.DETAILS\n3.EMAIL")