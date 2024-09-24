def record_no_check(record_no_input):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    command20 = "select record_no,admission_no,book_code,issue_date,return_date from issue_records where record_no=" + record_no_input + " and return_status=0"
    cur_lms.execute(command20)
    global RECORD
    RECORD = cur_lms.fetchone()
    if not RECORD:
        return 0
    else:
        return RECORD
def show_child():
    import mysql.connector as sql
    details = sql.connect(host='localhost', user='root', password='tiger', database='details')
    cur_details = details.cursor()
    command21 = "select name, class, section from students where admission_no=" + str(RECORD[1])
    cur_details.execute(command21)
    global CHILD
    CHILD=cur_details.fetchone()
    return CHILD
    #here type code to print in the app
def show_book():
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    command22 = "select name_of_book,author from books where book_code=" + str(RECORD[2])
    cur_lms.execute(command22)
    global BOOK
    BOOK=cur_lms.fetchone()
    return BOOK
    #herer type code to print in app
def fine_check():
    import datetime
    today_date = datetime.datetime.now()
    today_date = today_date.date()
    return_date=RECORD[4]
    if return_date >= today_date:
        return 0
    else:
        extra_days = today_date - return_date
        extra_days = extra_days.days
        extra_days = int(extra_days)
        fine = extra_days * 10
        return fine


def return_book():
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    command24 = "update issue_records set final_return_date=curdate(), return_status=1 where record_no=" + str(RECORD[0])
    cur_lms.execute(command24)
    lms.commit()
    command23 = "update books set quantity=quantity+1 where book_code=" + str(RECORD[2])
    cur_lms.execute(command23)
    lms.commit()


def send_email():
    import mysql.connector as sql
    email_list = sql.connect(host='localhost', user='root', password='tiger', database='email')
    cur_email = email_list.cursor()
    command26 = "select * from availability where required_book_code=" + str(RECORD[2]) + " and email_status=0"
    cur_email.execute(command26)
    required_book_code = cur_email.fetchone()
    if not required_book_code:
        pass
    else:
        details = sql.connect(host='localhost', user='root', password='tiger', database='details')
        cur_details = details.cursor()
        want_admission_no = required_book_code[1]
        command27 = "select name, class, section, email from students where admission_no=" + str(want_admission_no)
        cur_details.execute(command27)


        to = cur_details.fetchone()


        import smtplib
        subject = "Book Available in School Library"
        body = "Dear " + to[0] + " of Class " + str(to[1]) + " Section " + to[2] + " , The Book '" + BOOK[
            0] + "' is now available in the School Library you might get it issued."
        gmail_user = 'lms2022v.01@gmail.com'
        gmail_password = 'uqjrelaxptlizvyc'
        sent_from = gmail_user
        message = 'Subject: {}\n\n{}'.format(subject, body)
        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(gmail_user, gmail_password)
            smtp_server.sendmail(sent_from, to[3], message)
            smtp_server.close()
            print("Email Sent Successfully!")
        except Exception as ex:
            print("Something went wrong...", ex)


