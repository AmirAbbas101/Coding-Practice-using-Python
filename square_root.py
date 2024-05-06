# 8. Write a Python program to calculate the square root of a number.

def square_root(num):
    from math import sqrt
    return sqrt(num) 

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Square Root of {num} is {square_root(num)}")

    