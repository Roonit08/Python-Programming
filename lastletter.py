# write a python program function that takes a string as a parameter and returns the last character of the string. 

def get_last_character(text):
    return text[-1]            #method to get last character

text = input("Enter a word:")        #main program
result= get_last_character(text)
print("The last character is:",result)
