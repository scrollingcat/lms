def show_all_books():
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    cur_lms.execute("select * from books")
    return cur_lms.fetchall()