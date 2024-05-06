def factorial(num):
    if num < 0:
        print("Factorial is not defined for negative numbers.")
        return
    fact = 1
    i = num
    while i >= 1:
        fact *= i
        i -= 1
    print(f"Factorial of {num} is : {fact}")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    factorial(num)
