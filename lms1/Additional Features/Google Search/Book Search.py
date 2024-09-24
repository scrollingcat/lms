def search():
    Google = "https://www.google.com/search?q=" + H + "&oq=" + H + "&aqs=chrome.0.69i59.297j0j7&sourceid=chrome&ie=UTF-8"
    Amazon = "https://www.amazon.in/s?k=" + H + "&sprefix=Ha%2Caps%2C210&ref=nb_sb_ss_ts-doa-p_3_2"
    Flipkart = "https://www.flipkart.com/search?q=" + H + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    print("""1. Google
    2. Amazon
    3. Flipkart""")
    website = int(input("Enter Preference: "))
    from selenium import webdriver
    driver = webdriver.Chrome("chromedriver.exe")
    if website==1:
        driver.get(Google)
    elif website==2:
        driver.get(Amazon)
    elif website==3:
        driver.get(Flipkart)

def book_search(book_search_name):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms=lms.cursor()
    global H
    H=book_search_name
    book_search_name="'%"+book_search_name+"%'"
    command60="select * from books where name_of_book like "+book_search_name
    cur_lms.execute(command60)
    search_result=cur_lms.fetchall()
    if not search_result:
        question=input("Sorry but this book is not available in the library yet.\nWould you like to look it up online?")
        if question == "y" or question == "Y":
            H = H + " Book"
            H = H.replace(" ", "+")
            search()

    else:
        for view in search_result:
            print(view)

book_search("Bonjour")




#TODO Change H to variable from front end