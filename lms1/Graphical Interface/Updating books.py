#check_book_code()

def book_finder(book_code):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    command03="select name_of_book, author  from book where book_code="+str(book_code)
    BOOK=cur_lms.fetchone()
    return BOOK


def update_book_name(book_code,new_book_name):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    new_book_name='"'+new_book_name+'"'
    command04="update books set name_of_book="+new_book_name+" where book_code="+str(book_code)
    cur_lms.execute(command04)
    lms.commit()

def update_author(book_code,author_name):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    author_name = '"' +author_name+ '"'
    command05 = "update books set author=" + author_name+ " where book_code=" + str(book_code)
    cur_lms.execute(command05)
    lms.commit()

def update_publication(book_code,publication_name):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    publication_name = '"' +publication_name+ '"'
    command06 = "update books set publication=" + publication_name+ " where book_code=" +str( book_code)
    cur_lms.execute(command06)
    lms.commit()

def update_ISBN(book_code,ISBN):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    ISBN = '"' + ISBN + '"'
    command07 = "update books set ISBN=" + ISBN + " where book_code=" + str(book_code)
    cur_lms.execute(command07)
    lms.commit()

def update_tags(book_code,new_tag):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    new_tag = '"' + new_tag + '"'
    command08 = "update books set tags=" + new_tag + " where book_code=" + str(book_code)
    cur_lms.execute(command08)
    lms.commit()

def increase_quantity(book_code, increase_by):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    command09 = "update books set quantity=quantity+" + str(increase_by) + " where book_code=" + str(book_code)
    cur_lms.execute(command09)
    lms.commit()

def decrease_quantity(book_code,decrease_by):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    command010 = "update books set quantity=quantity-" + str(decrease_by) + " where book_code=" + str(book_code)
    cur_lms.execute(command010)
    lms.commit()
decrease_quantity(1,4)