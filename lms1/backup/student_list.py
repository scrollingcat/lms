def show_students():
    import mysql.connector as sql
    details = sql.connect(host='localhost', user='root', password='tiger', database='details')
    cur_details = details.cursor()
    cur_details.execute("select * from students")
    return cur_details.fetchall()

