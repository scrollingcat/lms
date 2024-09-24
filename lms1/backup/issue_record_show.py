def show_all_records():
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    details = sql.connect(host='localhost', user='root', password='tiger', database='details')
    cur_details = details.cursor()
    command01="select * from issue_records"
    cur_lms.execute(command01)
    record_details=cur_lms.fetchall()
    return record_details