# Checking if the entered word from the user is palindrome or not.

word = input("Enter a word: ")  #input from user

reversed_word = word.lower()[::-1]  # This method is used to reverse the word
if word.lower() == reversed_word:    # comparing the original and reversed word and .lower function allows both upper and lower case letter while checking
    print("The word is palindrome.")
else:
    print("The word is not palindrome.")
