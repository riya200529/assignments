# Write a Python program to sort a dictionary (ascending /descending) by value.
d = {'a': 3, 'b': 1, 'c': 2}

asc = dict(sorted(d.items(), key=lambda x: x[1]))
print("Ascending:", asc)
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print("Descending:", desc)
