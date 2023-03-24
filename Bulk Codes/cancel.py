import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(host='localhost', user='root', password='Samaraso$45', database='hotel')
my_cursor = mydb.cursor()

def cancel():
    print('\n ===== CANCEL BOOKING =====')
    b = ['Room']
    print('''Select booking:
        1. Room''')
    ch = int(input('Enter choice:'))
    print()
    if ch == 1:
        code=int(input('Enter booking code:'))
        com = f'''select code,Name,Regdate,Room,checkin,checkout,status,Days,Total from guest where code="{code}";'''
        print('\nYour details are:')

        my_cursor.execute(com)
        result = my_cursor.fetchall()

        print(tabulate(result,headers=['code','name','Regdate','Room','CheckIn','CheckOut','Status','Days','Total'],tablefmt='grid'))
        
        my_cursor.execute('Select total,room from guest where code={}'.format(code))
        result=my_cursor.fetchall()
        if result==[]:
            cancel()
        conf=input('Are you sure you want to cancel? (yes/no):')
        if conf in ('yes','Yes','YES'):
            print('Cancellation charge of 10% should be paid.\n')
            cancellation(result[0][0],result[0][1],'guest','room','roomno',code)
        exit()

def cancellation(cost,no,table,main,col,code):
    charge=0.1*float(cost)
    print(f'Charge to be paid: {charge} BD\n')
    name = input('Enter card holder name:')
    cardno = input('Enter card number:')
    pin = input('Enter card pin:')
    print('\nPayment successful !!')
    my_cursor.execute('delete from {} where code={};'.format(table,code))
    mydb.commit()
    my_cursor.execute('update {} set status="Vacant" where {}="{}";'.format(main,col,no))
    mydb.commit()
    print('\nYour booking has been canceled !')
    print('\nTHANK YOU FOR BOOKING WITH US !!')


