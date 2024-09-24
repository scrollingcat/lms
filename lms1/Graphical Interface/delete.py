def delete_book(book_code):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    command011 = "delete from books  where book_code=" + str(book_code)
    cur_lms.execute(command011)
    lms.commit()
    lms.close()