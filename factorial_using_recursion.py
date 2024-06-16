# 17. Write a Python program to find the factorial of a number using recursion.

def factorial(num):
    if num == 1 or num == 0:
        return 1
    elif num < 0:
        return "Invailid Number"
    
    return num * factorial(num - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")