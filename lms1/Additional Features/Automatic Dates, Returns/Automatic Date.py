import datetime

Issue_date=datetime.datetime.now()
Issue_date=Issue_date.date()
Return_date=Issue_date+datetime.timedelta(days=14)

Issue_date=str(Issue_date)
Return_date=str(Return_date)

import mysql.connector as sql
mydb=sql.connect(host='localhost', user='root' ,password='tiger',database='lms')
cur=mydb.cursor()
command=(1, 1, Issue_date,Return_date)
command=str(command)
print(command)

command="insert into issue_records (Admission_No,Book_Code,Issue_Date,Return_Date) values"+command
print(command)
#cur.execute(command)