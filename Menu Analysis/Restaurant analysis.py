# ============================================================
# TEC102 - Fundamentals of Programming
# Assessment 3 - Restaurant Data Analysis Program
# Student: [Your Name]
# Nepali Restaurant - Himalayan Bites
# ============================================================

# Import required modules
import csv
import os


# ============================================================
# FUNCTION: generate_data
# Purpose : Creates the menu.csv file with all restaurant data
#           This runs automatically if menu.csv does not exist
# ============================================================
def generate_data():

    # Define the field names (column headers)
    fields = ['item', 'price', 'category', 'avg_rating',
              'sales_mon', 'sales_tue', 'sales_wed',
              'sales_thu', 'sales_fri', 'sales_sat', 'sales_sun']

    # Define the data rows (item, price in AUD, category, rating, daily sales)
    rows = [
        ['Momo',           8.50,  'Starter',  4.8, 30, 28, 35, 32, 45, 60, 55],
        ['Chowmein',       10.00, 'Main',     4.3, 20, 22, 18, 25, 35, 40, 38],
        ['Laphing',        7.00,  'Starter',  4.5, 15, 18, 14, 20, 28, 35, 30],
        ['Thukpa',         12.00, 'Main',     4.2, 12, 15, 10, 14, 22, 30, 25],
        ['Choila',         14.00, 'Starter',  4.7, 10, 12,  8, 11, 18, 25, 20],
        ['Keema Noodles',  11.50, 'Main',     4.1,  8, 10,  9, 12, 20, 28, 22],
        ['Achar',           4.00, 'Starter',  4.3, 25, 22, 20, 24, 30, 40, 35],
        ['Sekuwa',         16.00, 'Main',     4.8, 14, 16, 12, 18, 28, 38, 32],
        ['Sel Roti',        5.50, 'Dessert',  4.6, 18, 20, 15, 22, 30, 42, 36],
        ['Dhido',          13.00, 'Main',     4.1, 10, 12,  8, 14, 18, 24, 20],
        ['Thakali Set',    22.00, 'Main',     4.9,  8, 10,  7, 12, 20, 30, 25],
        ['Dal Bhat',       18.00, 'Main',     4.7, 22, 25, 20, 28, 35, 48, 42],
        ['Chatamari',       9.00, 'Starter',  4.5, 12, 14, 10, 15, 22, 30, 26],
        ['Sukuti',         15.00, 'Starter',  4.5,  8, 10,  7, 11, 16, 22, 18],
        ['Chicken Chilli', 13.50, 'Main',     4.7, 18, 20, 16, 22, 32, 44, 38],
        ['Samosa',          5.00, 'Starter',  4.2, 20, 22, 18, 24, 30, 38, 32],
    ]

    # Create the CSV file and write the data rows
    with open('menu.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        writer.writerows(rows)

    print("  menu.csv has been created successfully!")


# ============================================================
# FUNCTION: load_data
# Purpose : Read and load all menu data from the CSV file
# ============================================================
def load_data(filename):
    data = []
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert numeric fields from string to correct data types
                row['price']      = float(row['price'])
                row['avg_rating'] = float(row['avg_rating'])
                row['sales_mon']  = int(row['sales_mon'])
                row['sales_tue']  = int(row['sales_tue'])
                row['sales_wed']  = int(row['sales_wed'])
                row['sales_thu']  = int(row['sales_thu'])
                row['sales_fri']  = int(row['sales_fri'])
                row['sales_sat']  = int(row['sales_sat'])
                row['sales_sun']  = int(row['sales_sun'])
                data.append(row)

    except FileNotFoundError:
        print("\n  [ERROR] menu.csv not found. Something went wrong.")

    return data


# ============================================================
# FUNCTION: display_table
# Purpose : Display all menu data in a neat table format
# ============================================================
def display_table(data):
    print("\n")
    print("=" * 72)
    print("           HIMALAYAN BITES - NEPALI RESTAURANT MENU DATA")
    print("=" * 72)

    # Print column headers
    print(f"  {'#':<4} {'Item':<18} {'Category':<12} {'Price (AUD)':<14} {'Avg Rating'}")
    print("  " + "-" * 65)

    # Print each menu item row
    for i, row in enumerate(data, start=1):
        print(f"  {i:<4} {row['item']:<18} {row['category']:<12} "
              f"${row['price']:<13.2f} {row['avg_rating']:.1f} / 5.0")

    print("  " + "-" * 65)
    print(f"  Total items on menu: {len(data)}")
    print("=" * 72)


# ============================================================
# FUNCTION: average_rating
# Purpose : Calculate and display average rating for each item
# ============================================================
def average_rating(data):
    print("\n")
    print("=" * 55)
    print("       AVERAGE CUSTOMER RATINGS PER MENU ITEM")
    print("=" * 55)

    # Print column headers
    print(f"  {'Item':<20} {'Rating':<10} {'Stars'}")
    print("  " + "-" * 48)

    # Sort items by rating from highest to lowest
    sorted_data = sorted(data, key=lambda x: x['avg_rating'], reverse=True)

    for row in sorted_data:
        # Build a simple star display using asterisks
        filled = int(row['avg_rating'])
        empty  = 5 - filled
        stars  = ('*' * filled) + ('-' * empty)
        print(f"  {row['item']:<20} {row['avg_rating']:<10.1f} [{stars}]")

    # Calculate the overall restaurant average
    overall = sum(r['avg_rating'] for r in data) / len(data)
    print("  " + "-" * 48)
    print(f"  Overall Restaurant Rating: {overall:.2f} / 5.00")
    print("=" * 55)


# ============================================================
# FUNCTION: total_sales_per_day
# Purpose : Calculate total sales and revenue for each day
# ============================================================
def total_sales_per_day(data):
    print("\n")
    print("=" * 52)
    print("        TOTAL SALES PER DAY OF THE WEEK")
    print("=" * 52)

    # Day labels paired with their matching CSV column key
    days = [
        ('Monday',    'sales_mon'),
        ('Tuesday',   'sales_tue'),
        ('Wednesday', 'sales_wed'),
        ('Thursday',  'sales_thu'),
        ('Friday',    'sales_fri'),
        ('Saturday',  'sales_sat'),
        ('Sunday',    'sales_sun'),
    ]

    # Print column headers
    print(f"  {'Day':<14} {'Items Sold':<14} {'Revenue (AUD)'}")
    print("  " + "-" * 46)

    best_day   = ''
    best_sales = 0

    for day_name, day_key in days:
        # Total items sold on this day across all menu items
        total_items   = sum(row[day_key] for row in data)
        # Total revenue = quantity sold * price for each item
        total_revenue = sum(row[day_key] * row['price'] for row in data)

        print(f"  {day_name:<14} {total_items:<14} ${total_revenue:,.2f}")

        # Track which day had the most sales
        if total_items > best_sales:
            best_sales = total_items
            best_day   = day_name

    print("  " + "-" * 46)
    print(f"  Busiest Day of the Week: {best_day} ({best_sales} items sold)")
    print("=" * 52)


# ============================================================
# FUNCTION: most_popular_item
# Purpose : Find the most popular item based on customer rating
# ============================================================
def most_popular_item(data):
    print("\n")
    print("=" * 52)
    print("     MOST POPULAR MENU ITEM (CUSTOMER RATINGS)")
    print("=" * 52)

    # Find item with the highest average rating
    top_item = max(data, key=lambda x: x['avg_rating'])

    # Find item with the highest total weekly sales
    most_sold = max(data, key=lambda x: (
        x['sales_mon'] + x['sales_tue'] + x['sales_wed'] + x['sales_thu'] +
        x['sales_fri'] + x['sales_sat'] + x['sales_sun']
    ))

    # Calculate total orders for the most sold item
    total_sold = (
        most_sold['sales_mon'] + most_sold['sales_tue'] + most_sold['sales_wed'] +
        most_sold['sales_thu'] + most_sold['sales_fri'] + most_sold['sales_sat'] +
        most_sold['sales_sun']
    )

    # Build star display for top rated item
    filled = int(top_item['avg_rating'])
    stars  = ('*' * filled) + ('-' * (5 - filled))

    print(f"\n  TOP RATED ITEM (by Customer Rating):")
    print(f"  {'Item':<12}: {top_item['item']}")
    print(f"  {'Category':<12}: {top_item['category']}")
    print(f"  {'Price':<12}: ${top_item['price']:.2f} AUD")
    print(f"  {'Rating':<12}: {top_item['avg_rating']} / 5.0  [{stars}]")

    print(f"\n  MOST ORDERED ITEM (by Total Weekly Sales):")
    print(f"  {'Item':<12}: {most_sold['item']}")
    print(f"  {'Category':<12}: {most_sold['category']}")
    print(f"  {'Total Sold':<12}: {total_sold} orders this week")
    print(f"  {'Rating':<12}: {most_sold['avg_rating']} / 5.0")
    print("=" * 52)


# ============================================================
# FUNCTION: display_menu
# Purpose : Print the main interactive menu options
# ============================================================
def display_menu():
    print("\n")
    print("*" * 52)
    print("*      HIMALAYAN BITES - DATA ANALYSIS SYSTEM      *")
    print("*" * 52)
    print("*   1. Display Full Menu Data (Table)              *")
    print("*   2. View Average Ratings Per Item               *")
    print("*   3. View Total Sales Per Day of Week            *")
    print("*   4. Find Most Popular Menu Item                 *")
    print("*   5. Exit Program                                *")
    print("*" * 52)


# ============================================================
# FUNCTION: get_valid_choice
# Purpose : Validate user input - only accept integers 1 to 5
# ============================================================
def get_valid_choice():
    while True:
        try:
            choice = input("\n  Enter your choice (1-5): ").strip()

            # Check for empty input
            if choice == '':
                print("  [!] Input cannot be empty. Please enter a number from 1 to 5.")
                continue

            # Try converting to integer
            choice = int(choice)

            # Check if within valid range
            if 1 <= choice <= 5:
                return choice
            else:
                print("  [!] Invalid choice. Please enter a number between 1 and 5.")

        except ValueError:
            # Catches letters or symbols
            print("  [!] Invalid input. Please enter a number, not text.")


# ============================================================
# MAIN FUNCTION
# Purpose : Entry point - generates data then runs the loop
# ============================================================
def main():

    # Step 1: Generate menu.csv if it does not already exist
    if not os.path.exists('menu.csv'):
        print("\n  Generating restaurant data file (menu.csv)...")
        generate_data()
    else:
        print("\n  menu.csv already exists. Skipping data generation.")

    # Step 2: Load the data from menu.csv
    data = load_data('menu.csv')

    # If data is empty something went wrong - stop the program
    if not data:
        print("\n  [ERROR] Could not load data. Please check menu.csv exists.")
        return

    print("  Data loaded! Welcome to Himalayan Bites Analysis System.\n")

    # Step 3: Main loop - keeps running until user selects option 5
    while True:
        display_menu()
        choice = get_valid_choice()

        if choice == 1:
            display_table(data)

        elif choice == 2:
            average_rating(data)

        elif choice == 3:
            total_sales_per_day(data)

        elif choice == 4:
            most_popular_item(data)

        elif choice == 5:
            print("\n  Thank you for using Himalayan Bites Analysis System!")
            print("  Goodbye!\n")
            break

        # Pause before returning to the menu
        input("\n  Press Enter to return to the main menu...")


# ============================================================
# Run the program
# ============================================================
if __name__ == '__main__':
    main()