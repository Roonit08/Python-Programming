#write a lamda function that takes a number as a parameter and returns true if the number if even else return false.

text= int(input("Enter a number:"))
is_even = lambda x: x % 2 == 0
print(is_even(text))