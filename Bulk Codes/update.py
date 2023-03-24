from datetime import datetime
from tabulate import tabulate
import mysql.connector
import math

mydb = mysql.connector.connect(host='localhost', user='root', password='Samaraso$45', database='hotel')
my_cursor = mydb.cursor()


def update():
    code = int(input('Enter your booking code:'))
    com = f'''select code,Name,Regdate,Room,checkin,checkout,status,Days,
                                  Total from guest where code="{code}";'''
    print('\nYour current details are:')

    my_cursor.execute(com)
    result = my_cursor.fetchall()

    print(tabulate(result, headers=['code', 'name', 'Regdate', 'Room',
                                    'CheckIn', 'CheckOut', 'Status', 'Days', 'Total(BD)'],tablefmt='fancy_grid'))

    while True:
        print()
        print('\nselect detail to edit:')
        print('1. Name   2. CheckIn date   3. CheckOut date')
        ch = int(input('Enter choice:'))
        print()

# ================== UPDATE NAME ==================
        if ch == 1:
            name = input('Enter new name:')
            com_name = f"update guest set name='{name}' where code={code};"
            my_cursor.execute(com_name)
            mydb.commit()
            com = f'''select code,Name,Regdate,Room,checkin,checkout,status,Days,
                                  Total from guest where code="{code}";'''
            print('\nYour current details are:')

            my_cursor.execute(com)
            result = my_cursor.fetchall()

            print(tabulate(result, headers=['code', 'name', 'Regdate', 'Room',
                                    'CheckIn', 'CheckOut', 'Status', 'Days', 'Total(BD)'],tablefmt='fancy_grid'))
            


# ================== UPDATE CHECK IN DATE ==================
        elif ch == 2:
            cin=print('Enter the Check in Date')
            y = int(input('Year: '))
            m = int(input('Month: '))
            d = int(input('Date: '))
            cind = ''+str(datetime(y,m,d))+''

            com_cin = f"update guest set checkin='{cind}' where code={code};"
            my_cursor.execute(com_cin)
            mydb.commit()
            out =result[0][5]

            if str(out)<cind:
                print('\nChange CheckOut date as well')

            else:
                com_days = f"update guest set days=checkout-checkin where code={code};"
                my_cursor.execute(com_days)
                mydb.commit()

                com = f'''select code,Name,Regdate,Room,checkin,checkout,status,Days,
                                  Total from guest where code="{code}";'''
                print('\nYour current details are:')

                my_cursor.execute(com)
                result = my_cursor.fetchall()

                print(tabulate(result, headers=['code', 'name', 'Regdate', 'Room',
                                    'CheckIn', 'CheckOut', 'Status', 'Days', 'Total(BD)'],tablefmt='fancy_grid'))
                exit()

# ================== UPDATE CHECK OUT TIME ==================
        elif ch == 3:
            cout=print('Enter the Check out Date')
            y = int(input('Year: '))
            m = int(input('Month: '))
            d = int(input('Date: '))
            coutd = ''+str(datetime(y,m,d))+''
            com_cout = f"update guest set checkout='{coutd}' where code={code};"
            my_cursor.execute(com_cout)
            mydb.commit()
            ind = result[0][4]

            if str(coutd) < str(ind):
                print('Change CheckOut date:')
                com_days = f"update guest set days=checkout-checkin where code={code};"
                my_cursor.execute(com_days)
                mydb.commit()

            else:
                com_days = f"update guest set days=checkout-checkin where code={code};"
                my_cursor.execute(com_days)
                mydb.commit()
                com = f'''select code,Name,Regdate,Room,checkin,checkout,status,Days,
                                  Total from guest where code="{code}";'''
                print('\nYour current details are:')

                my_cursor.execute(com)
                result = my_cursor.fetchall()

                print(tabulate(result, headers=['code', 'name', 'Regdate', 'Room',
                                    'CheckIn', 'CheckOut', 'Status', 'Days', 'Total(BD)'],tablefmt='fancy_grid'))
                exit()

