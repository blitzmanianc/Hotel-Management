import datetime
import mysql.connector
import checkin
from tabulate import tabulate

mydb = mysql.connector.connect(host='localhost', user='root', password='Samaraso$45', database='hotel')
mycursor = mydb.cursor()

# ============== CHECK OUT ==================
def checkout():
    print('====== CHECK OUT ======')
    code = int(input('Enter booking code:'))
    mycursor.execute('SELECT status FROM guest where code={}'.format(code))
    st = mycursor.fetchall()
    if st == []:
        print('\nInvaild Code !! Pls retry !')
        checkin.checkin()
    elif st[0][0] == 'Not Checked In':
        print('\nYou have not checked in yet!!')
        exit()

    today = datetime.date.today()
    mycursor.execute('SELECT checkout FROM guest where code={}'.format(code))
    cout = mycursor.fetchall()
    if today < cout[0][0]:
        print(f'\nYour check out date is on {cout[0][0]}.')
        ch=input('Are you sure you want to check out ? (yes/no):')
        if ch in ('no','No','NO'):
            exit()
        if ch in ('yes', 'Yes','YES'):
            guest=[]
            query='select * from guest where code={}'.format(code)
            mycursor.execute(query)
            myrec=mycursor.fetchall()
            for i in myrec:
                print(tabulate(guest, headers=['Total']))
                print(i[8])
            name = input('Enter card holder name:')
            cardno = input('Enter card number:')
            pin = input('Enter card pin:')
            print('\nPayment successful !!')
            
    if today >= cout[0][0]:
        print(f'\nYour check out date is on {cout[0][0]}.')
        ch=input('Are you sure you want to check out ? (yes/no):')
        if ch in ('no','No','NO'):
            exit()
        if ch in ('yes', 'Yes','YES'):
            guest=[]
            query='select * from guest where code={}'.format(code)
            mycursor.execute(query)
            myrec=mycursor.fetchall()
            for i in myrec:
                print(tabulate(guest, headers=['Total']))
                print(i[8])
            name = input('Enter card holder name:')
            cardno = input('Enter card number:')
            pin = input('Enter card pin:')
            print('\nPayment successful !!')
    

    mycursor.execute('Select room from guest where code={}'.format(code))
    room = mycursor.fetchall()[0][0]
    mycursor.execute('DELETE from guest where code={}'.format(code))
    mydb.commit()
    mycursor.execute('update room set status="Vacant" where roomno="{}";'.format(room))
    mydb.commit()
    search()

def search():
    com = f'''select code,Name,Regdate,Room,checkin,checkout,status,Days,Total from guest;'''
    print('\nYour details are:')

    mycursor.execute(com)
    result = mycursor.fetchall()

    print(tabulate(result,headers=['code','name','Regdate','Room','CheckIn','CheckOut','Status','Days','Total'],tablefmt='grid'))
    print('\nTHANK YOU FOR BOOKING WITH US !!')


