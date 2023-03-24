# Hotel-Management

The code is for booking hotel rooms and storing the booking details in a MySQL database. It allows users to search for available rooms, select a room, enter their booking details, and store them in the database.
(This code was first made for a project in grade 12, the code serves as an example only)
The code is a Python program that helps to manage hotel room bookings. It connects to a MySQL database to store and retrieve data about available rooms, customer details, and booking information. The program allows users to search for available rooms, select a room type and room option, and make a booking by providing customer details and check-in/check-out dates. The program calculates the total cost of the booking and updates the database to reflect the new booking and room availability status. The program also provides a search function to retrieve and display customer and booking details.

This code implements a hotel management system using Python and MySQL database. It defines various functions for booking, room service, check-in, check-out, search, update, and cancel. The mysql.connector module is used to connect to the database.

The main() function displays a menu with different options and prompts the user to select one of them. Based on the user's input, it calls the corresponding function to perform the required operation. If the user selects option 5, it displays another submenu with search, edit, and cancel options. The functions for these options are defined in separate modules.

The code also defines an Exit() function that allows the user to return to the main menu or exit the program.

This code is a Python script for booking hotel rooms and keeping records of guest information in a MySQL database.

The code imports the necessary modules such as mysql.connector, datetime, and tabulate. It also defines a search module that is used in the userEntry() function, but this module is not provided in this code.

The script defines several functions such as searchroom(), roomselect(), bookingRecord(), and userEntry(). The roomselect() function allows the user to select a room based on room type and options, and then calls the searchroom() function to check if the selected room is vacant. If the selected room is not vacant, the roomselect() function is called again to prompt the user to select a different room. If the room is vacant, the searchroom() function prompts the user to enter the room number, and then calls the userEntry() function to enter guest information.

The bookingRecord() function prompts the user to enter the check-in and check-out dates, calculates the number of days the guest will stay, and calculates the total cost of the stay based on the room price and number of days.

The userEntry() function prompts the user to enter the guest's name and registration date, calls the bookingRecord() function to calculate the total cost and booking dates, generates a random booking code, and inserts the guest information into the MySQL database. Finally, it calls the search module (not provided in this code) to search for the guest's booking in the database.

Overall, this code provides a basic framework for booking hotel rooms and keeping records of guest information in a MySQL database. However, there are some issues that need to be addressed such as error handling, input validation, and security considerations for storing sensitive guest information in a database.
