# write a function that takes a string as a parameter and returns the length of the string 


def get_string_length(text):   #function to return length of a string
    return len(text)

text= input("Enter a word:")   #main program
result= get_string_length(text)
print("The length is:",result)