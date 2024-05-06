# Method One
def reverse_string(given_string):
    return given_string[::-1]

# Method two for core logic building.
def reverse_string1(given_string):
    given_string = list(given_string)
    start = 0
    end = len(given_string) - 1
    swap = ""
    # new_string = list
    for i in range(end):
        swap = given_string[start]
        if (end == start):
            break

        elif start <  end:
            given_string[start] = given_string[end]
            given_string[end] = swap
            start +=1
            end -= 1
    return "".join(given_string)

if __name__ == "__main__":
    get_string = input("Enter a string : ")
    print(reverse_string1(get_string))

