# 5. Write a Python program to check if a string is a palindrome.

def isPalindrome(given_string):
    return given_string == given_string[::-1]

if __name__ == "__main__":
    given_string = input("Enter a String : ")
    
    if isPalindrome(given_string):
        print("Given string is a palindrome string.")

    else:
        print("Given string is not a plaindrome string.")