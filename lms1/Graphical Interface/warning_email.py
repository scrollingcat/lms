def warning_email_send():
    import datetime
    today_date = datetime.datetime.now()
    today_date = today_date.date()
    today_date_string = str(today_date)
    date_file = open("date_file.txt", 'r')
    date_in_file = date_file.read()
    if date_in_file == today_date_string:
        date_file.close()
    else:
        date_file.close()
        return_dates = today_date + datetime.timedelta(days=1)
        return_dates = str(return_dates)
        return_dates = "'" + return_dates + "'"
        import mysql.connector as sql
        lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
        details = sql.connect(host='localhost', user='root', password='tiger', database='details')
        cur_lms = lms.cursor()
        cur_details = details.cursor()
        command50 = "select record_no, admission_no, book_code, return_date from issue_records where return_date=" + return_dates + " and return_status=0"
        cur_lms.execute(command50)
        email_records = cur_lms.fetchall()
        if len(email_records) == 0:
            pass
        else:
            for record in email_records:
                record_no = record[0]
                admission_no = record[1]
                book_code = record[2]
                return_date = record[3]
                command51 = "select name, class, section,email from students where admission_no=" + str(admission_no)
                cur_details.execute(command51)
                to = cur_details.fetchone()
                command52 = "select name_of_book from books where book_code=" + str(book_code)
                cur_lms.execute(command52)
                kitaab = cur_lms.fetchone()
                import smtplib
                subject = "Book Return due Tomorrow"
                body = "Dear " + to[0] + " of Class " + str(to[1]) + " Section " + to[
                    2] + ", this is a reminder to return The Book '" + kitaab[
                           0] + "' whose return is due tomorrow i.e. " + str(
                    return_date) + "\nYour Record No. is " + str(
                    record_no) + "\nReturn the book tomorrow or bring the book to the Library to get an extension.\nNote: If the Book is not returned by tomorrow or brought to the library to get an extension, then fine has to be paid."
                gmail_user = 'lms2022v.01@gmail.com'
                gmail_password = 'uqjrelaxptlizvyc'
                sent_from = gmail_user
                # to = STUDENT_DETAILS[3]
                message = 'Subject: {}\n\n{}'.format(subject, body)
                try:
                    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    smtp_server.ehlo()
                    smtp_server.login(gmail_user, gmail_password)
                    smtp_server.sendmail(sent_from, to[3], message)
                    smtp_server.close()
                    print("Email Sent Successfully!")
                except:
                    return "ERROR"
            date_file = open("date_file.txt", 'w')
            date_file.write(today_date_string)
            date_file.close()

