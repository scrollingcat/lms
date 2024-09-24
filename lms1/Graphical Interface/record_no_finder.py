def record_no_finder(admission_no):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='lms')
    cur_lms = lms.cursor()
    command28="select * from issue_records where admission_no="+str(admission_no)+" and return_status=0"
    cur_lms.execute(command28)
    issued_book_record=cur_lms.fetchall()
    if not issued_book_record:
       return 0
    else:
        the_list=[]
        details=sql.connect(host='localhost', user='root', password='tiger', database='details')
        cur_details=details.cursor()
        command62="select name,class,section from students where admission_no="+str(admission_no)
        cur_details.execute(command62)
        kid=cur_details.fetchone()
        kid_found=(kid[0],kid[1],kid[2])
        the_list.append(kid_found)
        result_no=1
        a_list=[]
        for k in issued_book_record:
            command61 = "select name_of_book from books where book_code="+str(k[2])
            cur_lms.execute(command61)
            bookname=cur_lms.fetchone()
            bookname=bookname[0]
            issue_record_found=(result_no,bookname,k[0],k[3],k[4])
            a_list.append(issue_record_found)
            result_no+=1
        the_list.append(a_list)
        return the_list