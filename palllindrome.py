#write a lamda function that takes a string as parameter and returns the palindrome or print false

text = input("Enter a word:")
is_palindrome = lambda s: s if s.lower() == s.lower()[::-1] else False

print(is_palindrome(text))