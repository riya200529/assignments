# Write a Python program to unzip a list of tuples into individual
data = [(1, 2), (3, 4), (5, 6)]

list1, list2 = map(list, zip(*data))

print(list1)
print(list2)