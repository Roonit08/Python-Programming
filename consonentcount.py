# write a function that takes a string as a parameter and returns the total number of consonants in the string.


def first_consonent(text):
    consonent="qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
    count=0
    for char in text:
      if char in consonent:
        count +=1
    return count

text = input("Ebter a word:")
result=first_consonent(text)
print("The first consonent is:",result)