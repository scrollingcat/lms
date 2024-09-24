import sys
def add_students(no_of_students):
    import mysql.connector as sql
    mydb=sql.connect(host='localhost', user='root', password='tiger', database='details')
    cur=mydb.cursor()
    for i in range(no_of_students):
        Admission_No=input("*Enter Admission No: ")
        Name=input("*Enter Student Name: ")
        Name='"'+Name+'"'
        Class=input("*Enter Class of Student: ")
        Section=input("*Enter Section of Student: ")
        Section='"'+Section+'"'
        Phone_No=input("Enter Phone No. of Student: ")
        if Phone_No=="":
            Phone_No="null"
        else:
            Phone_No='"'+Phone_No+'"'
        Email=input("Enter E-mail address of Student: ")
        if Email=="":
            Email="Null"
        else:
            Email = '"' + Email + '"'
        command12="insert into students (Admission_no,name,class,section,phone_no,Email) values ("+Admission_No+" , "+Name+" , "+Class+" , "+Section+" , "+Phone_No+" , "+Email+")"
        try:
            cur.execute(command12)
            mydb.commit()
        except:
            print("You did a mistake!")
            again=input("Wanny Try Again: ")
            if again=='y' or again=='Y':
                NOS = int(input("Enter the no. of records to be inserted: "))
                add_students(NOS)
            else:
                sys.exit(1)
                print("Bye")

NOS=int(input("Enter the no. of records to be inserted: "))
add_students(NOS)