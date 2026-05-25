# write a function that takes a string as a parameter and returns the first consonant of the string.

def first_consonent(text):
    consonent="qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
    for char in text:
      if char in consonent:
        return char
    return "no consonent"

text = input("Ebter a word:")
result=first_consonent(text)
print("The first consonent is:",result)