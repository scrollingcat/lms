import csv
with open("hello.csv",'w',newline='') as f:
    w=csv.writer(f,delimiter=',')
    w.writerows([[1,2,3,4],[0,9,8,7]])