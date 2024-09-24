import smtplib

#receiver_email=input("Enter E-mail address to be sent to: ")

subject=input("Enter subject of the E-mail: ")
body=input("Enter Body of the E-main: ")



gmail_user='lms2022v.01@gmail.com'
gmail_password='uqjrelaxptlizvyc'
sent_from=gmail_user
#to=[receiver_email]

message = 'Subject: {}\n\n{}'.format(subject,body)
print(type(message))
print(message)

"""try:
    smtp_server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user,gmail_password)
    smtp_server.sendmail(sent_from,to,message)
    smtp_server.close()
    print("Email Sent Successfully!")
except Exception as ex:
    print("Something went wrong...",ex)"""




#TODO Variable to be taken from front end