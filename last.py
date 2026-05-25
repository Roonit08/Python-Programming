#write a lamda function that takes a string as a parameter and returns the last character of the string.


text=input("Enter a word:")
last_char = lambda s: s[-1]

print(last_char(text))
