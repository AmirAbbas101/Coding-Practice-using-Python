# 4. Write a Python program to find the sum of digits in a number.

def sum_of_digits(number):
    number = str(number)
    sum = 0
    for i in number:
        sum += int(i)
    return sum

def sum_of_digits_2(number):
    sum = 0
    while number != 0:
        sum += number % 10
        num = number /10

    return sum

if __name__ == "__main__":
    number = int(input("Enter a Number: "))
    print(f"Sum of digits in {number} is: {sum_of_digits_2(number)}")
