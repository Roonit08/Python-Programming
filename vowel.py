# write a function that takes a string as a parameter and returns the first vowel of the string.

def first_vowel(text):
    vowels="aeiouAEIOU"
    for char in text:
       if char in vowels:
         return char
    return "no vowels"

text=input("Enter a word:")
result=first_vowel(text)
print("The first vowel is:",result)