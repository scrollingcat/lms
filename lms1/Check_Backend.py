def show_databases():
    import mysql.connector as sql
    mydb = sql.connect(host="localhost",
                       user='root',
                       password='tiger')
    mycursor = mydb.cursor()
    mycursor.execute("Show Databases")
    b = 1
    for i in mycursor:
        print(b, '\t', i[0])
        b += 1


global db_name


def show_tables(db_name):
    import mysql.connector as sql
    mydb = sql.connect(host="localhost",
                       user='root',
                       password='tiger',
                       database=db_name)
    mycursor = mydb.cursor()
    mycursor.execute("Show Tables")
    b = 1
    c = mycursor.fetchall()
    for i in c:
        print(b, '\t', i[0])
        b += 1


global tb_name


def desc_table(tb_name):
    import mysql.connector as sql
    mydb = sql.connect(host="localhost",
                       user='root',
                       password='tiger',
                       database=db_name)
    mycursor = mydb.cursor()
    desc = "desc " + tb_name
    mycursor.execute(desc)
    for i in mycursor:
        print(i)


def records(tb_name):
    import mysql.connector as sql
    mydb = sql.connect(host="localhost",
                       user="root",
                       password="tiger",
                       database=db_name)
    cur = mydb.cursor()
    comm1 = "select * from " + tb_name + ";"
    cur.execute(comm1)
    y = cur.fetchall()
    if len(y) == 0:
        print("No Records Found")
    else:
        for x in y:
            print(x)


show_databases()
import sys

try:
    db_name = input("Enter Database Name: ")
    show_tables(db_name)
    try:
        tb_name = input("Enter Table Name: ")
        desc_table(tb_name)
        try:
            r = input("wanna see records: ")
            if r == 'y' or r == 'Y':
                records(tb_name)
        except:
            print("BIEE...")
            sys.exit(1)
    except:
        print("BIEE...")
        sys.exit(1)
except:
    print("BIEE...")
    sys.exit(1)
