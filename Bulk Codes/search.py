import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(host='localhost', user='root', password='Samaraso$45', database='hotel')
mycursor = mydb.cursor()

def search():
    code = int(input('Enter your booking code:'))
    com = f'''select code,Name,Regdate,Room,checkin,checkout,status,Days,Total from guest where code="{code}";'''
    print('\nYour details are:')

    mycursor.execute(com)
    result = mycursor.fetchall()

    print(tabulate(result,headers=['code','name','Regdate','Room','CheckIn','CheckOut','Status','Days','Total'],tablefmt='grid'))
