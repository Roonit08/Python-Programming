# Task 2 
# Simple energy calculator

print("--Smart Energy Calculator--")
while True:
    # Displaying Menu here 
    print("\nMenu:")
    print("1.Calculate energy used by appliance")
    print("2.Estimate total daily electricity cost")
    print("3.Exit")
    choice = input("\nEnter your choice (1-3):") # user need to enter 1 2 or 3 according to the menu

    # Option 1: Appliance Energy Calculation is Done here
    if choice == "1":
        appliance = input("Enter appliance name: ")  
        power = float(input("Enter power rating (in watts): "))
        hours = float(input("Enter hours used: "))

        # Formula used is: Energy = (Power × Time) ÷ 1000
        energy = (power * hours) / 1000
        print(f"\nYour {appliance} used {energy:.2f} kWh today.")

    # Option 2: Cost Calculation is done in this part
    elif choice == "2":
        total_kwh = float(input("Enter total energy consumption (kWh): ")) 
        rate = float(input("Enter cost per kWh: "))
        total_cost = total_kwh * rate
        print(f"\nEstimated total cost= Rs. {total_cost:.2f}")

    # Option 3: Exit Program
    elif choice == "3":
        print("\n Thank you! ") # this is printed if you finish calculating
        break

    # If user enters anything other than 1-3 this appears
    else:
        print("\nInvalid choice!!!, please try again.")

        
