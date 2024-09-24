def addbooks(Name_of_Book,Author,Publisher,ISBN,Quantity,Tags):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur = lms.cursor()
    Name_of_Book='"'+Name_of_Book+'"'
    if Author=='':
        Author="Default"
    else:
        Author='"'+Author+'"'

    if Publisher=='':
        Publisher="Default"
    else:
        Publisher='"'+Publisher+'"'
        
    if ISBN=='':
        ISBN="Default"
    else:
        ISBN='"'+ISBN+'"'

    Quantity=str(Quantity)
    if Quantity=="":
        Quantity="Default"
    else:
        pass
    if Tags=='':
        Tags="Default"
    else:
        Tags='"'+Tags+'"'


    command1="insert into books (Name_of_book,Author,Publisher,ISBN,Quantity,Tags) values "+"("+Name_of_Book+" , "+Author+" , "+Publisher+" , "+ISBN+" , "+Quantity+" , "+Tags+")"
    cur.execute(command1)
    lms.commit()
    lms.close()