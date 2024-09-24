def check_admission_no(admission_no):
    import mysql.connector as sql
    details = sql.connect(host='localhost', user='root', password='tiger', database='details')
    cur_details = details.cursor()
    command13 = "select * from students where admission_no=" + admission_no
    cur_details.execute(command13)
    adcheck = cur_details.fetchone()
    if not adcheck:
        return 0
    else:
        return 1
def check_book_code(book_code):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    command14 = "select * from books where book_code=" + book_code
    cur_lms.execute(command14)
    codecheck = cur_lms.fetchone()
    if not codecheck:
        return 0
    else:
        return 1
def book_availability(admission_no, book_code):
    import mysql.connector as sql
    details = sql.connect(host='localhost', user='root', password='tiger', database='details')
    cur_details = details.cursor()
    command12 = "select name,class,section,email from students where admission_no=" + admission_no
    cur_details.execute(command12)
    global STUDENT_DETAILS
    STUDENT_DETAILS = cur_details.fetchone()
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    command_12 = "select Name_of_Book,Author,Quantity from books where book_code=" + book_code
    cur_lms.execute(command_12)
    global BOOK_DETAILS
    BOOK_DETAILS = cur_lms.fetchone()
    Qty = BOOK_DETAILS[2]
    if Qty == 0:
        return ["no copy",STUDENT_DETAILS[0],STUDENT_DETAILS[1],STUDENT_DETAILS[2],BOOK_DETAILS[0],BOOK_DETAILS[1]]
    else:
        return ["yes_copy",STUDENT_DETAILS[0],STUDENT_DETAILS[1],STUDENT_DETAILS[2],BOOK_DETAILS[0],BOOK_DETAILS[1]]
def availability_email(admission_no,book_code):
    import mysql.connector as sql
    e_mail = sql.connect(host='localhost', user='root', password='tiger', database='email')
    cur_email = e_mail.cursor()
    command25 = "insert into availability (admission_no,required_book_code) values(" + admission_no + "," + book_code + ")"
    cur_email.execute(command25)
    e_mail.commit()
def issue_book(admission_no,book_code):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    import datetime
    issue_date = datetime.datetime.now()
    issue_date = issue_date.date()
    return_date = issue_date + datetime.timedelta(days=14)
    issue_date = str(issue_date)
    return_date = str(return_date)
    final_return_date = return_date
    command14 = (admission_no, book_code, issue_date, return_date)
    command14 = str(command14)
    command14 = "insert into issue_records (admission_no, book_code, issue_date, return_date) values" + command14
    cur_lms.execute(command14)
    command15 = "update books set quantity=quantity-1 where book_code=" + book_code
    cur_lms.execute(command15)
    lms.commit()
    command17 = "select record_no from issue_records order by record_no desc"
    cur_lms.execute(command17)
    record_no = cur_lms.fetchone()
    print("Book Issued.")
    statement = "Your Book Issue Serial No. is: " + str(record_no[0])
    print(statement)
    print("FINAL DATE TO RETURN THE BOOK: ", final_return_date,
          "\nNOTE: If book not returned by return date Fine has to be paid. A fine of Rs. 10/day has to be paid after due date.")

    #Email
    import smtplib
    subject = "Book Issued From School Library"
    if str(BOOK_DETAILS[1]) == "None":
        body = "Dear " + str(STUDENT_DETAILS[0]) + " of Class " + str(STUDENT_DETAILS[1]) + " Section " + str(
            STUDENT_DETAILS[2]) + " , The Book '" + str(BOOK_DETAILS[
                                                            0]) + "' " + " has been successfully issued to you.\n" + statement + "\nThe FINAL RETURN DATE OF THE BOOK IS: " + str(
            final_return_date) + "\nNOTE: If book not returned by return date i.e. " + str(
            final_return_date) + ", fine has to be paid. A fine of Rs. 10/day has to be paid after due date."
    else:
        body = "Dear " + str(STUDENT_DETAILS[0]) + " of Class " + str(STUDENT_DETAILS[1]) + " Section " + str(
            STUDENT_DETAILS[2]) + " , The Book '" + str(BOOK_DETAILS[0]) + "' by " + str(BOOK_DETAILS[
                                                                                             1]) + " has been successfully issued to you.\n" + statement + "\nThe FINAL RETURN DATE OF THE BOOK IS: " + str(
            final_return_date) + "\nNOTE: If book not returned by return date i.e. " + str(
            final_return_date) + ", fine has to be paid. A fine of Rs. 10/day has to be paid after due date."
    gmail_user = 'lms2022v.01@gmail.com'
    gmail_password = 'uqjrelaxptlizvyc'
    sent_from = gmail_user
    to = STUDENT_DETAILS[3]
    message = 'Subject: {}\n\n{}'.format(subject, body)
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, message)
        smtp_server.close()
        print("Email Sent Successfully!")
    except Exception as ex:
        print("Something went wrong...", ex)



    #Email List Update
    email_list = sql.connect(host='localhost', user='root', password='tiger', database='email')
    cur_email = email_list.cursor()
    command42 = "select * from availability where required_book_code=" + book_code + " and admission_no=" + admission_no + " and email_status=0"
    cur_email.execute(command42)
    required_book_code = cur_email.fetchone()
    if required_book_code == None:
        pass
    else:
        email_record_no = required_book_code[0]
        command43 = "update availability set email_status=1 where serial_no=" + str(email_record_no)
        cur_email.execute(command43)
        email_list.commit()