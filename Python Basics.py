
# Task 1: Introduction to Python 3
# Asking the user to enter their name and greeting them

def task1():
    print("\nTask 1:Greeting Program")
    while True:
        name = input("Enter your name (or type 'back' to return to menu):") # User is asked to input name 
        name = name.strip()
        if name.lower() == "back": # if user dont wanna continue ends the program
            break
        if name == "":
            print("Name cannot be empty.So,Please try again.") # if no input is entered this message pops
            continue
        print("Hello, " + name +"!") # output of greeting along with users name
        break

# Task 2: Control Flow
# Asking the user for their age and finding out he/she is minor or adult

def task2():
    print("\nTask 2: Minor or Adult")
    while True:
        age_input = input("Enter your age (or type 'back' to return to menu):") # User is asked to input their age 
        age_input = age_input.strip()
        if age_input.lower() == "back":  # if user dont wanna continue ends the program
            break
        if age_input == "":
            print("Age cannot be empty.So,Please try again.") # if no input is entered this message pops
            continue
        age = int(age_input)
        if age < 18:
            print("You are a minor (under 18).") # if user age is less then 18
        else:
            print("You are an adult (18 or older).") # if user age is more then 18
        break

# Task 3: Lists
# Building a list of 5 numbers and printing the sum of the first three numbers
 
def task3():
    print("\nTask 3: List and Sum")
    print("Enter 5 whole numbers one by one.") # User is asked to input 5 numbers
    while True:
        numbers = []
        go_back = False
        for i in range(1, 6):  # makes sure only 5 different numbers are entered
            entry_done = False
            while not entry_done:
                user_input = input("Enter number" + str(i) + "(or 'back' for menu):") # 5 different numbers are entered
                user_input = user_input.strip()
                if user_input.lower() == "back": # if user dont wanna continue ends the program
                    go_back = True
                    entry_done = True
                    continue
                if user_input == "":  # if no input is entered this message pops
                    print("Cannot be empty. Please enter a number.")
                    continue
                numbers.append(int(user_input)) # adds numbers at the end of the list
                entry_done = True
            if go_back:
                break
        if go_back:
            break
        # sum of first three using slicing and a loop
        total = 0
        for num in numbers[:3]:
            total = total + num
        print("\nYour list of 5 numbers:")
        print(numbers)
        print("Sum of first three(" + str(numbers[0]) + " + " + str(numbers[1]) + " + " + str(numbers[2]) + ") = " + str(total)) # adding the first 3 numbers
        break

# Task 4: Loops
# Asking the user for a number and printing its multiplication table

def task4():
    print("\nTask 4: Multiplication Table") 
    while True:
        user_input = input("Enter a number (or type 'back' to return to menu):") # user is asked to enter a number whose multiplication table is intended
        user_input = user_input.strip()
        if user_input.lower() == "back": # if user dont wanna continue ends the program
            break
        if user_input == "":
            print("Input cannot be empty. Please enter a number.") # if no input is entered this message pops
            continue
        # handling input where user enters negative number instead
        temp = user_input
        if temp[0] == "-":
            temp = temp[1:]
        if temp == "":
            print("Please enter a valid number.")
            continue
        num = int(user_input)
        print("\nMultiplication table for" + str(num) + ":") 
        for i in range(1, 11): # table till the range of 10 is limited
            print(str(num) + " x " + str(i) + " = " + str(num * i)) # multiplixation table is printed 
        break

# Task 5: Functions
# Using find_max() function to return the largest number in a list

# Helper Function: find_max Defined here so it is available when user calls it
def find_max(numbers):
    # start by assuming the first number is the largest
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num  # update if a bigger number is found
    return max_value

def task5():
    print("\nTask 5: Find Maximum Number")
    print("Enter numbers one by one. Type 'done' when finished (at least 2 numbers needed).")  # user is asked to enter a list of numbers at least 2 minimum
    while True:
        numbers = []
        go_back = False
        while True:
            if len(numbers) == 0:
                prompt = "Enter a number (or 'back' for menu): "  # used to enter first number and if user dont wanna continue ends the program
            else:
                prompt = "Enter another number (or 'done' to finish): " # used to enter more then 1 number and end the list when user wants
            user_input = input(prompt)
            user_input = user_input.strip()
            if user_input.lower() == "back": # if user dont wanna continue ends the program 
                go_back = True
                break
            if user_input.lower() == "done": # if user is done entering numbers in the list it stops 
                if len(numbers) < 2: # makes sure at least 2 numbers are entered
                    print("Please enter at least 2 numbers before typing 'done'.")
                    continue
                break
            if user_input == "": # if no input is entered this message pops
                print("Cannot be empty. Enter a number.")
                continue
            temp = user_input
            if temp == "":
                print("Please enter a valid number.")
                continue
            numbers.append(int(user_input)) # adds numbers at the end of the list
            print("Added. List so far:")
            print(numbers)
        if go_back:
            break
        result = find_max(numbers) # this helps to find the biggest number in the list 
        print("\nYour list:")
        print(numbers)
        print("The maximum number is:" + str(result)) # display the output maximum number 
        break

# Task 6: Strings
# Asking the user for a sentence and counting the vowels in it

def task6():
    print("\nTask 6: Count Vowels")
    while True:
        sentence = input("Enter a sentence (or type 'back' to return to menu):") # user is asked to enter a sentence
        if sentence.lower() == "back": # if user dont wanna continue ends the program
            break
        if sentence.strip() == "":  # if no input is entered this message pops
            print("Sentence cannot be empty. Please try again.")
            continue
        vowels = "aeiouAEIOU" # all the upper and lower case vowels stored
        count = 0
        for char in sentence: 
            if char in vowels: 
                count = count + 1 # this checks every letter of sentence and if it matches with vowel count increase
        print("Sentence entered: " + sentence)
        print("Number of vowels: " + str(count)) # output result of no of vowels in a user entered sentence
        break

# Main Menu

def main():
    print("Fundamentals of Programming:Assessment 2")
    while True:
        print("\nMain Menu: Select a task to run") # this is the main menu with different task to access and run the program
        print("1. Task 1 - Week 1: Greeting Program")
        print("2. Task 2 - Week 2: Minor or Adult")
        print("3. Task 3 - Week 3: List and Sum")
        print("4. Task 4 - Week 4: Multiplication Table")
        print("5. Task 5 - Week 5: Find Maximum Number")
        print("6. Task 6 - Week 7: Count Vowels")
        print("7. Exit")
        choice = input("\nEnter your choice (1-7):") # according to menu number range input is to be entered
        choice = choice.strip() 
        if choice =="1":
            task1()
        elif choice =="2":
            task2()
        elif choice =="3":
            task3()
        elif choice =="4":
            task4()
        elif choice =="5":
            task5()
        elif choice =="6":
            task6()
        elif choice =="7":
            print("Exit")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.") # if any number apart from the range is entered it shows this error message

# start the program
main()