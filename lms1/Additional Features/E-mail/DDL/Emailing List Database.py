import mysql.connector as sql
email_list=sql.connect(host='localhost', user='root', password='tiger')
cur_email=email_list.cursor()
cur_email.execute("create database email")
cur_email.execute("use email")
cur_email.execute("create table availability(serial_no int primary key auto_increment, admission_no int not null, required_book_code int, email_status bit(1) default 0)")