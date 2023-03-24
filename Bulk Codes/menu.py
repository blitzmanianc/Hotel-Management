import Booking
import Roomservice
import checkin
import checkout
import search
import update
import cancel
import mysql.connector

con = mysql.connector.connect(host='localhost', user='root',password='Samaraso$45', database='hotel')
cur = con.cursor()

def main():
    print('\n===== MAIN MENU =====')
    print('''1. Booking
2. Room Service
3. Check In
4. Check Out
5. Manage Booking
0. Exit\n''')
    menu=int(input("Enter choice: "))
    if menu==1:
        Booking.roomselect()
    elif menu==2:
        Roomservice.roomservice()
    elif menu==3:
        checkin.checkin()
    elif menu==4:
        checkout.checkout()
    elif menu==5:
        print('''1. Search
2. Edit
3. Cancel''')
        ch=int(input("Enter choice: "))
        if ch==1:
            search.search()
        elif ch==2:
            update.update()
        elif ch==3:
            cancel.cancel()
            
    elif menu==0:
        def Exit():
            print()
            print('\nDo you want to return to main menu ?')
            exchoice = input('yes/no? :')
            if exchoice in ('yes', 'YES', 'Yes'):
                main()
            else:
                print('\n Thank You !!')
        Exit()
main()
        
