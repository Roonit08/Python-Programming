
# This creates a csv file with the restaurant menu data
import csv
import os

# The filename is stored in a constant variable so it can be easily changed if needed
FILENAME = "menu.csv"

# This function creates the restaurant menu data and saves it to a CSV file which was created above also Each menu item stores 5 individual customer ratings so the program can calculate the average
def create_data():
    headers = ["Item", "Category", "Price", "R1", "R2", "R3", "R4", "R5",
               "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    rows = [
        ["Momo",           "Starter", 8.50,  5, 5, 4, 5, 5, 30, 28, 35, 32, 45, 60, 55],
        ["Chowmein",       "Main",    10.00, 4, 5, 4, 4, 4, 20, 22, 18, 25, 35, 40, 38],
        ["Laphing",        "Starter", 7.00,  5, 4, 5, 4, 4, 15, 18, 14, 20, 28, 35, 30],
        ["Thukpa",         "Main",    12.00, 4, 4, 4, 5, 4, 12, 15, 10, 14, 22, 30, 25],
        ["Choila",         "Starter", 14.00, 5, 5, 4, 5, 5, 10, 12,  8, 11, 18, 25, 20],
        ["Keema Noodles",  "Main",    11.50, 4, 4, 4, 4, 5, 8,  10,  9, 12, 20, 28, 22],
        ["Achar",          "Starter",  4.00, 4, 5, 4, 4, 4, 25, 22, 20, 24, 30, 40, 35],
        ["Sekuwa",         "Main",    16.00, 5, 5, 5, 4, 5, 14, 16, 12, 18, 28, 38, 32],
        ["Sel Roti",       "Dessert",  5.50, 5, 4, 5, 5, 4, 18, 20, 15, 22, 30, 42, 36],
        ["Dhido",          "Main",    13.00, 4, 4, 4, 4, 5, 10, 12,  8, 14, 18, 24, 20],
        ["Thakali Set",    "Main",    22.00, 5, 5, 5, 5, 5,  8, 10,  7, 12, 20, 30, 25],
        ["Chatamari",      "Starter",  9.00, 4, 5, 4, 5, 4, 12, 14, 10, 15, 22, 30, 26],
        ["Sukuti",         "Starter", 15.00, 5, 4, 4, 5, 4,  8, 10,  7, 11, 16, 22, 18],
        ["Chicken Chilli", "Main",    13.50, 5, 5, 4, 5, 5, 18, 20, 16, 22, 32, 44, 38],
        ["Samosa",         "Starter",  5.00, 4, 4, 5, 4, 4, 20, 22, 18, 24, 30, 38, 32],
    ]
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print("Data file created successfully.")

# This function reads data from the CSV file and returns it as a list and also converts each column to the correct data type and handles missing file errors
def read_data():
    data = []
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # this skips the header row
            for row in reader:
                row[2]  = float(row[2])  # price
                row[3]  = int(row[3])    # rating 1
                row[4]  = int(row[4])    # rating 2
                row[5]  = int(row[5])    # rating 3
                row[6]  = int(row[6])    # rating 4
                row[7]  = int(row[7])    # rating 5
                row[8]  = int(row[8])    # Monday
                row[9]  = int(row[9])    # Tuesday
                row[10] = int(row[10])   # Wednesday
                row[11] = int(row[11])   # Thursday
                row[12] = int(row[12])   # Friday
                row[13] = int(row[13])   # Saturday
                row[14] = int(row[14])   # Sunday
                data.append(row)
    except FileNotFoundError:
        print("Error: " + FILENAME + " was not found. Please restart the program.")
    return data

# This function calculates the average rating for a single menu item also It adds up the 5 individual customer ratings and divides by 5 to get the average rating for each items 
def calculate_item_rating(row):
    total = row[3] + row[4] + row[5] + row[6] + row[7]
    return total / 5

# This function prints the main menu options for the user
def display_menu():
    print("\n-- Himalayan Bites - Data Analysis Menu --")
    print("1. Display all menu data")
    print("2. Average rating per item")
    print("3. Total sales per day")
    print("4. Most popular item")
    print("5. Exit")

# This function handles user input and makes sure only a valid number is accepted and keeps asking until the user enters a number between 1 and 5
def get_valid_choice():
    while True:
        try:
            choice = input("Enter your choice (1-5): ").strip()
            # This Checks if the user entered nothing and entered an empty string 
            if choice == "":
                print("Input cannot be empty. Please enter a number from 1 to 5.")
                continue
            choice = int(choice)
            # This Checks if the number is within the valid range of 1 to 5
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            # This catches letters or special characters because only numbers are valid input for the menu
            print("Invalid input. Please enter a number, not text.")

# This function displays all menu items in a clean table format  
def display_table(data):
    print("\nHimalayan Bites - Full Menu Data")
    print("-" * 60)
    print(f"{'Item':<18}     {'Category':<10}          {'Price (AUD)':<14}") # The extra space here is to make the menu table look neat and seperated form the other columns
    print("-" * 60)
    for row in data:
        # Calculates the average rating from the 5 stored customer ratings
        avg = calculate_item_rating(row)
        print(f"{row[0]:<18}     {row[1]:<10}          ${row[2]:<13.2f}")
    print("-" * 60)
    print(f"Total items on menu: {len(data)}")

# This function calculates and displays the average rating for each menu item
# Also It calculates the average from 5 individual customer ratings per item
# And the items are sorted from highest to lowest so the best rated items appear first
def calculate_average_rating(data):
    print("\nAverage Customer Rating Per Menu Item")
    print("-" * 40)
    # This Sorts items by their calculated average rating, highest first
    sorted_data = sorted(data, key=lambda row: calculate_item_rating(row), reverse=True)
    for row in sorted_data:
        avg = calculate_item_rating(row)
        print(f"{row[0]:<18} {avg:.2f} / 5.00")
    # This Calculates the overall average rating across all menu items
    overall = sum(calculate_item_rating(row) for row in data) / len(data)
    print("-" * 40)
    print(f"Overall Restaurant Average: {overall:.2f} / 5.00")

# This function calculates total items sold and revenue generated for each day  and also identifies the busiest day of the week
def calculate_sales_per_day(data):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("\nTotal Sales Per Day of the Week")
    print("-" * 45)
    print(f"{'Day':<14} {'Items Sold':<14} {'Revenue (AUD)'}")
    print("-" * 45)
    busiest_day =""
    highest_sales =0
    for i, day in enumerate(days):
        # Sales columns start at index 8 in the row
        total_items = sum(row[8 + i] for row in data)
        # Revenue is calculated by multiplying quantity sold by price for each item
        total_revenue = sum(row[8 + i] * row[2] for row in data)
        print(f"{day:<14} {total_items:<14} ${total_revenue:,.2f}")
        # Update the busiest day if today has more sales than the previous best
        if total_items > highest_sales:
            highest_sales = total_items
            busiest_day = day
    print("-" * 45)
    print(f"Busiest Day: {busiest_day} with {highest_sales} items sold")

# This function finds and displays the most popular menu item also here the Popularity is determined by calculating the average of 5 customer ratings per item
def find_most_popular_item(data):
    best_item = data[0]
    for row in data:
        # Compares calculated average to find the highest rated item
        if calculate_item_rating(row) > calculate_item_rating(best_item):
            best_item = row
    avg = calculate_item_rating(best_item)
    print("\nMost Popular Menu Item (Based on Customer Rating)")
    print("-" * 45)
    print(f"Item     : {best_item[0]}")
    print(f"Category : {best_item[1]}")
    print(f"Price    : ${best_item[2]:.2f} AUD")
    print(f"Rating   : {avg:.2f} / 5.0")

# So now this is the Main function that runs the program and handles all user interaction
def main():
    # this Creates the data file only if it does not already exist
    if not os.path.exists(FILENAME):
        create_data()
    # this loads the data from the CSV file
    data = read_data()
    # this helps to Stop the program if the data could not be loaded
    if not data:
        return
    print("Welcome to Himalayan Bites Data Analysis System!")
    # this part Keeps the program running until the user chooses to exit
    while True:
        display_menu()
        choice = get_valid_choice()
        if choice == 1:
            display_table(data)
        elif choice == 2:
            calculate_average_rating(data)
        elif choice == 3:
            calculate_sales_per_day(data)
        elif choice == 4:
            find_most_popular_item(data)
        elif choice == 5:
            print("Thank you for using Himalayan Bites Analysis System. Goodbye!")
            break
# Start the program
main()
