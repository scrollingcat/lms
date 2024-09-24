import datetime

today_date = datetime.datetime.now()
today_date = today_date.date()
new_return_date = today_date + datetime.timedelta(days=14)
new_return_date=str(new_return_date)
new_return_date='"'+new_return_date+'"'


def extend(record_no):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    command30 = "update issue_records set return_date=" + new_return_date + "where record_no=" + record_no
    cur_lms.execute(command30)
    lms.commit()


def extend_email(record_no):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    details = sql.connect(host='localhost', user='root', password='tiger', database='details')
    cur_lms = lms.cursor()
    cur_details = details.cursor()
    command101 = "select record_no,admission_no,book_code from issue_records where record_no=" + record_no
    cur_lms.execute(command101)
    RECORD = cur_lms.fetchone()
    command12 = "select name,class,section,email from students where admission_no=" + str(RECORD[1])
    cur_details.execute(command12)
    child = cur_details.fetchone()
    to = child[3]
    command_12 = "select Name_of_Book from books where book_code=" + str(RECORD[2])
    cur_lms.execute(command_12)
    BOOK_DETAILS = cur_lms.fetchone()
    import smtplib
    subject = "Extension Granted for Issued Book"
    body = "Dear " + str(child[0]) + " of Class " + str(
        child[1]) + " Section " + str(
        child[2]) + " , you have been successfully granted an extension of 14 days for the Book '" + str(
        BOOK_DETAILS[
            0]) + "' " + "\nThe NEW FINAL RETURN DATE OF THE BOOK IS: " + str(
        new_return_date) + "\nNOTE: If book not returned by return date i.e. " + str(
        new_return_date) + ", fine has to be paid. A fine of Rs. 10/day has to be paid after due date."
    gmail_user = 'lms2022v.01@gmail.com'
    gmail_password = 'uqjrelaxptlizvyc'
    sent_from = gmail_user
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
