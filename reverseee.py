#write a lamda function that takes a string as parameter and returns the reverse of the string.

text= input("Enter a word:")
reverse_string = lambda s: s[::-1]

print(reverse_string(text))
