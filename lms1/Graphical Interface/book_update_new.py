def book_code_check(Book_Code):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    Book_Code=str(Book_Code)
    command2="select * from books where book_code="+Book_Code
    cur_lms.execute(command2)
    details_of_book=cur_lms.fetchone()
    if not details_of_book:
        return 0
    else:
        original_book_data=details_of_book
        return original_book_data
def update_book_name(Name_of_Book,Book_Code):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    Name_of_Book = '"' + Name_of_Book + '"'
    command4 = "update books set Name_of_Book=" + Name_of_Book + " where book_code=" + Book_Code
    cur_lms.execute(command4)
    lms.commit()
def update_author_name(Author,Book_Code):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    Author = '"' + Author + '"'
    command5 = "update books set Author=" + Author + "where book_code=" + Book_Code
    cur_lms.execute(command5)
    lms.commit()
def update_publication_name(Publisher,Book_Code):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    Publisher = '"' + Publisher + '"'
    command6 = "update books set Publisher=" + Publisher + "where book_code=" + Book_Code
    cur_lms.execute(command6)
    lms.commit()
def update_ISBN_number(ISBN,Book_Code):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    ISBN = '"' + ISBN + '"'
    command6 = "update books set ISBN=" + ISBN + "where book_code=" + Book_Code
    cur_lms.execute(command6)
    lms.commit()
def update_quantity_of_book(Quantity,Book_Code):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    command7="update books set quantity="+Quantity+" where book_code="+Book_Code
    cur_lms.execute(command7)
    lms.commit()
def update_book_tag(new_tag,Book_Code):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    new_tag = '"' + new_tag + '"'
    command11 = "update books set tags=" + new_tag + "where book_code=" + Book_Code
    cur_lms.execute(command11)
    lms.commit()