# write a function that takes a string as a parameter and returns the total number of vowels in the string.


def first_vowel(text):
    vowels="aeiouAEIOU"
    count =0
    for char in text:
       if char in vowels:
         count +=1
    return count

text=input("Enter a word:")
result=first_vowel(text)
print("The first vowel is:",result)