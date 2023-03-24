from tabulate import tabulate
import datetime
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='Samaraso$45', database='hotel')
my_cursor = mydb.cursor()

# =========== ROOM SERVICE SUB ===============
def roomservice():
    print()
    print('\n===== ROOM SERVICE =====')
    print('''1. Order Food ''')

    choice = int(input('Enter Your Choice:'))
    if choice == 1:
        foodorder()
    else:
        print('Invalid !')
        roomservice()

# ========== ORDER FOOD =================
def foodorder():
    code = int(input('\nEnter your booking code:'))
    my_cursor.execute(f'select * from guest where code={code};')
    result = my_cursor.fetchall()
    if result == []:
        print('Invalid Booking code')
        roomservice()

    print('\n========== MENU ============')
    print('1: Indian Dish')
    print('2. Chinese Dish')
    print('3. Soups')
    print('4. Hot Beverages')
    print('5. Juices')
    dishes = {1: 'Indian Dish', 2: 'Chinese Dish', 3: 'Soup', 4: 'Hot Beverage', 5: 'Juice'}
    choice = int(input('\nEnter your choice of dish (0 to exit):'))

    hour = datetime.datetime.now().hour
    if choice == 1 and 0 <= hour < 12: # morning till 12 noon
        type = 'breakfast'
        command = f"Select item, price from food where type='{type}' and dish='{dishes[choice]}';"
    elif choice == 1 and 12 <= hour < 17: # 12 noon till 5pm
        type = 'lunch'
        command = f"Select item, price from food where type='{type}' and dish='{dishes[choice]}';"
    elif choice == 1 and 17 <= hour < 24: # 5pm till midnight
        type = 'dinner'
        command = f"Select item, price from food where type='{type}'  and dish='{dishes[choice]}';"
    elif choice == 0:
        roomservice()
    else:
        command = f"Select item, price from food where dish='{dishes[choice]}';"

    my_cursor.execute(command)
    foods = my_cursor.fetchall()
    print()

    food_list = []
    sno = 1
    for i in foods:
        l = [sno, i[0], i[1]]
        food_list.append(l)
        sno += 1

    print(tabulate(food_list, headers=['S.No', 'Item', 'Price (BD)'], tablefmt='psql'))

    order = []
    while True:
        food = int(input('\nEnter food sno\nor 0 to confirm order :'))
        if food == 0:
            break
        else:
            qty = int(input('Enter quantity:'))
            order.append([foods[food - 1][0], qty])

    print('\nYour order is:')
    print(tabulate(order, headers=['Item', 'quantity'], tablefmt='psql'))

    total = 0
    for i in order:
        for j in foods:
            if i[0] == j[0]:
                total += i[1] * j[1]
    print('total= ', round(total, 1), ' BD')
    print('\nThank you for ordering !! Your food will arrive soon !!')
    exit()
