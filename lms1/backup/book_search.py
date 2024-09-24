def search_book(book_search_name):
    import mysql.connector as sql
    lms = sql.connect(host='localhost', user='root', password='tiger', database='LMS')
    cur_lms = lms.cursor()
    global H
    H = book_search_name
    book_search_name = "'%" + book_search_name + "%'"
    command60 = "select * from books where name_of_book like " + book_search_name
    cur_lms.execute(command60)
    search_result = cur_lms.fetchall()
    if not search_result:
        return 0
    else:
        return search_result

def online_search(website, H):
    H=str(H)+" Book"
    from selenium import webdriver
    global driver
    driver = webdriver.Chrome("chromedriver.exe")
    if website=="Google":
        Google = "https://www.google.com/search?q=" + H + "&oq=" + H + "&aqs=chrome.0.69i59.297j0j7&sourceid=chrome&ie=UTF-8"
        driver.get(Google)
    elif website=="Amazon":
        Amazon = "https://www.amazon.in/s?k=" +H + "&sprefix=Ha%2Caps%2C210&ref=nb_sb_ss_ts-doa-p_3_2"
        driver.get(Amazon)
    elif website=="Flipkart":
        Flipkart = "https://www.flipkart.com/search?q=" + H + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        driver.get(Flipkart)