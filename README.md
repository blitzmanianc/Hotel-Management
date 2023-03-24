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
![f1672630-5bfc-491b-abb7-843e2230046b](https://user-images.githubusercontent.com/83311731/227460357-aa4f9203-fd02-43cd-bec0-b830f904d3c8.jpg)
![eee825af-2579-421d-9daa-2df259b87487](https://user-images.githubusercontent.com/83311731/227460381-d2efe2e8-ff0e-45c2-9487-8d2f688ce368.jpg)
![fe95d18c-651d-4b64-9dd2-24f91374be5e](https://user-images.githubusercontent.com/83311731/227460427-406048bf-6b16-4961-bcbc-6bcf3909fa9e.jpg)
![c0d4260e-8dfb-4207-ba70-9c754e77280e](https://user-images.githubusercontent.com/83311731/227460463-876aba08-55cf-4dff-a314-5d9077f3fa47.jpg)
![6ab9d120-a974-4e89-bd98-04c217aea3d8](https://user-images.githubusercontent.com/83311731/227460490-ed01f680-c692-457d-aac3-00d8281e4d16.jpg)
![4a1905e1-74bb-453c-8959-528a57e04ae0](https://user-images.githubusercontent.com/83311731/227460547-d87bd8a9-6397-4b7e-87c1-1776162efda8.jpg)
![d834e331-f276-4445-84c1-50c6cb079b0a](https://user-images.githubusercontent.com/83311731/227460575-f89a7a59-8a50-4da4-929d-4a9a44b2af34.jpg)
![7c4f8a10-39a2-4dc0-8865-2f9e79ad6f9e](https://user-images.githubusercontent.com/83311731/227460604-8c2b307a-e3bb-4dda-9c86-ab5ea29119f3.jpg)
![ad08b4fd-13df-4c27-b844-afe30831314a](https://user-images.githubusercontent.com/83311731/227460627-f56f8309-0cc3-48ed-b501-d9720000d601.jpg)
![76f9d0cd-0ec6-4576-95f8-8bf4d2df0b4c](https://user-images.githubusercontent.com/83311731/227460650-bdc03441-bdf3-4303-9b6d-2726e0f478bf.jpg)
![0154a7df-f38d-4476-9bb7-9d1ea2c8ecb9](https://user-images.githubusercontent.com/83311731/227460684-63c04c08-57cd-4ad1-8ca6-180c65cb2aab.jpg)
![c841534f-16ac-4905-849f-485d5d734a41](https://user-images.githubusercontent.com/83311731/227460700-5ffd9314-4683-47b3-ab03-2aab94efb466.jpg)
![f0d2aeda-4d4e-43ba-96cb-90de074de0bc](https://user-images.githubusercontent.com/83311731/227460729-f1214bb5-fba9-4795-8f85-77446bcff9b5.jpg)
![e3fafb58-9a83-4fb5-969c-364f39b33f50](https://user-images.githubusercontent.com/83311731/227461037-61e091fb-0076-41e2-b63a-48851ac58928.jpg)
![aae89068-e0d0-4ac9-b7a2-29f5c0974163](https://user-images.githubusercontent.com/83311731/227461075-5b4ef785-8b5e-4555-b02e-a2bc98bb5362.jpg)
![2050b647-487a-4eee-86c1-df41dc3782cb](https://user-images.githubusercontent.com/83311731/227461087-35ba957e-8b46-48c7-b918-ae8433a5ceda.jpg)
![fe4585b9-b055-4e0c-841e-2e3f4c1e6efc](https://user-images.githubusercontent.com/83311731/227461104-a1f8e46b-ff2c-4923-b399-6724b42f9421.jpg)



