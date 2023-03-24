import mysql.connector
from datetime import date
from tabulate import tabulate
import random
import search

con = mysql.connector.connect(host='localhost', user='root',password='Samaraso$45', database='hotel')
cur = con.cursor()
query = 'select * from room'
cur.execute(query)
myrec = cur.fetchall()
def searchroom():
    C = 0   
    global room
    global price
    print('Searching for Vacant Room..','...')
    for i in myrec:
        G = i[0],i[1],i[3]
        if i[1] == A and i[2] == B and i[3] == 'Vacant':
            G = i[0],i[1],i[3]
            C = C+1
            print(i[0])
    print('Total Number of Vacant Room',C)
    if C == 0:
        roomselect()
    room = input('Enter Room No: ')
    for i in myrec:
        if i[0] == room:
            price = i[4]            
    userEntry()



def roomselect():
    print ("##### We have The Following Rooms For You #####")
    print("1. Double Room")
    print("2. Penthouse")
    print("3. Single Room")
    print("4. Suite Room")
    P = int(input('\n Enter the Room No: '))
    global A
    global B

    if P == 1:
        A = 'Double Room'
        print('\n Options avaiable are \n 1. Single Bath \n 2. Double Bath')
        option = int(input('\n Enter the Room Option: '))
        if option == 1:
            B = 'Single Bath'
        if option == 2:
            B = 'Double Bath'
    
    if P == 2:
        A = 'Penthouse'
        print('\n Options avaiable are \n 1. Double Room + 1 kids Room \n 2. Triple Room + 2 kids Room')
        option = int(input('\n Enter the Room Option: '))
        if option == 1:
            B = 'Double Room + 1 kids Room'
        if option == 2:
            B = 'Triple Room + 2 kids Room'
    
    if P == 3:
        A = 'Single Room'
        print('\n Options avaiable are \n 1. Single Bed \n 2. Double Bed')
        option = int(input('\n Enter the Room Option: '))
        if option == 1:
            B = 'Single Bed'
        if option == 2:
            B = 'Double Bed'
    
    if P == 4:
        A = 'Suite Room'
        print('\n Options avaiable are \n 1. Single Room- Single Bath \n 2. Double Room- Double Bath \n 3. Triple Room- Triple Bath')
        option = int(input('\n Enter the Room Option: '))
        if option == 1:
            B = 'Single Room- Single Bath'
        if option == 2:
            B = 'Double Room- Double Bath'
        if option == 3:
            B = 'Triple Room- Triple Bath'
    searchroom()
    









def bookingRecord():
    global checkin
    global checkout
    global days
    global Total
    print('Enter the Check in Date')
    y = int(input('Year: '))
    m = int(input('Month: '))
    d = int(input('Date: '))
    checkin = ''+str(date(y,m,d))+''
    print('Enter the Check out Date')
    y2 = int(input('Year: '))
    m2 = int(input('Month: '))
    d2 = int(input('Date: '))
    checkout = ''+str(date(y2,m2,d2))+''
    days = d2-d
    Total = days*price

def userEntry():
    for i in range(1):
     name = input("Enter Customer Name : ")
     code = random.randint(1000,9999)
     regdate = input('Enter Customer Registration Date [ YYYY-MM-DD ] :')
     bookingRecord()
     status = 'Not Checked in'
     sql = "insert into guest values ('"+str(code)+"','"+name+"','"+regdate+"','"+room+"','"+checkin+"','"+checkout+"','"+status+"','"+str(days)+"','"+str(Total)+"')"
     sql2 = "update room set Status = 'Occupied' where Roomno = '"+str(room)+"'"
     cur.execute(sql)
     cur.execute(sql2)
     con.commit()
     print("booking code is:",code)
     search.search()


    print("\nNew Customer Entered In The System Successfully !")
