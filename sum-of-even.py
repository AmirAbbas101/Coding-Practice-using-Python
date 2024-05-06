def sumOfEven(num):
    sum = 0
    for i in range(2,num+1,2):
        sum += i
    return sum

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Sum of all even numbers from 1 to {num} is {sumOfEven(num)}")