# Write a Python function that takes a list and returns a new list with unique elements of the first list
def unique_list(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

# example
lst = [1, 2, 2, 3, 4, 3, 5]
print(unique_list(lst))
