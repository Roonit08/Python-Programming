# write a function that takes a string as a parameter and returns the reverse of the string.


def get_reverse(text):
    return text[::-1]  # method to reverse the string

text= input("Enter a word:")    # main program
result= get_reverse(text)
print("The reverse of the word is:",result)