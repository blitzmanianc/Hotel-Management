import datetime
import mysql.connector
import search

mydb = mysql.connector.connect(host='localhost', user='root', password='Samaraso$45', database='hotel')
mycursor = mydb.cursor()


# ============ CHECK IN ================
def checkin():
    print('\n====== CHECK IN ======')
    code = int(input('Enter booking code:'))
    mycursor.execute('SELECT status FROM guest where code={}'.format(code))
    st = mycursor.fetchall()
    if st == []:
        print('\nInvaild Code !! Pls retry !')
        checkin()
    elif st[0][0]== 'Checked In':
        print('\nYou have already checked in !!')
        exit()

    today = datetime.date.today()
    mycursor.execute('SELECT checkin FROM guest where code={}'.format(code))
    cin = mycursor.fetchall()
    if today < cin[0][0]:
        print(f'\nSorry!! Check In failed.\nYour check in date is on {cin[0][0]}.')
        exit()

    mycursor.execute('update guest set status="Checked In" where code={};'.format(code))
    mydb.commit()
    mycursor.execute('SELECT checkout FROM guest where code={}'.format(code))
    myresult = mycursor.fetchall()
    print('\nYour check out date is ', myresult[0][0])
    search.search()
    print('You have successfully checked in !!')

