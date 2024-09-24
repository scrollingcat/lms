def admission_no_finder(name):
    import mysql.connector as sql
    details = sql.connect(host='localhost', user='root', password='tiger', database='details')
    cur_details = details.cursor()
    name="'%"+name+"%'"
    command19="select * from students where name like "+name
    cur_details.execute(command19)
    student_record=cur_details.fetchall()
    if not student_record:
        print("NO Such Records found in the Student Database")
    else:
        for k in student_record:
            print(k)
a=input("enter your name: ")
admission_no_finder(a)