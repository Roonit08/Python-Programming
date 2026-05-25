# There are 3 students their name and marks are entered by user and checking their result.

pass_marks = 40 

# Student 1
name1 = input("Enter name of Student 1: ")
marks1 = float(input("Enter marks of Student 1: "))     # input data of student 1 form user
if marks1 >= pass_marks:                                # condition check for result
    print("Congratulations You have passed your exams.")
else:
    print("sorry you have Failed.")

# Student 2
name2 = input("\nEnter name of Student 2: ")                   
marks2 = float(input("Enter marks of Student 2: "))          # input data of student 2 form user
if marks2 >= pass_marks:                                     # condition check for result
    print("Congratulations You have passed your exams.")      
else:
    print("sorry you have Failed.")

# Student 3
name3 = input("\nEnter name of Student 3: ")
marks3 = float(input("Enter marks of Student 3: "))           # input data of student 3 form user
if marks3 >= pass_marks:                                      # condition check for result
    print("Congratulations You have passed your exams.")
else:
    print("sorry you have Failed.")