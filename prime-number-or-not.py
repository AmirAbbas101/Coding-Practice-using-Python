import math

def is_prime(num):
    if num < 2:  # Special case: numbers less than 2 are not prime
        return False
    if num == 2:  # Special case: 2 is prime
        return True
    if num % 2 == 0:  # Even numbers (except 2) are not prime
        return False
    
    # Check divisibility from 3 to the square root of the number
    sqrt_num = int(math.sqrt(num))
    for i in range(3, sqrt_num + 1, 2):  # Iterate odd numbers only
        if num % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
