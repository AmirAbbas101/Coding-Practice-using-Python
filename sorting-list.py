# 7. Write a Python program to sort elements in a list in ascending order.

def sort_lst(lst):
    lst.sort()
    print(lst)

if __name__ == "__main__":
    lst = [5,2,4,1,8,9,3,5]
    sort_lst(lst)