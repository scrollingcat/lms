import mysql.connector as sql
m=sql.connect(host="localhost", user="root", passwd="tiger")
print(m)