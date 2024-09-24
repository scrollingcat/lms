



import sys
H=input("Enter what book name to search for: ")
H=H+" Book"
H=H.replace(" ","+")

Google="https://www.google.com/search?q="+H+"&oq="+H+"&aqs=chrome.0.69i59.297j0j7&sourceid=chrome&ie=UTF-8"
Amazon="https://www.amazon.in/s?k="+H+"&sprefix=Ha%2Caps%2C210&ref=nb_sb_ss_ts-doa-p_3_2"
Flipkart="https://www.flipkart.com/search?q="+H+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

print("""1. Google
2. Amazon
3. Flipkart""")

def choice():
    global website
    website=int(input("Enter Preference: "))

def choice_check():
    if website>3 or website<1:
        print("Wrong input")
        again = input("Wanna try again: ")
        if again == 'y' or again == 'Y':
            choice()
            choice_check()
        else:
            sys.exit(1)
    else:
        pass

choice()
choice_check()



from selenium import webdriver
driver = webdriver.Chrome("chromedriver.exe")
#driver.implicitly_wait(0.5)



def search():
    if website==1:
        driver.get(Google)
    elif website==2:
        driver.get(Amazon)
    elif website==3:
        driver.get(Flipkart)
search()







#TODO Change H to variable from front end