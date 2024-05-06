def find_largest(lst):
    largest_element = lst[0]
    for num in lst:  
        if num > largest_element:
            largest_element = num
    
    return largest_element


lst = [3, 2, 2, 65, 2, 8, 2, 5, 2, 7, 89, 1234, 234, 23, 12]
print("The largest element in the list is:", find_largest(lst))
