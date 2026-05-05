# Write a Python program to find the highest 3 values in a dictiona
d = {'a': 10, 'b': 50, 'c': 30, 'd': 20}
values = sorted(d.values(), reverse=True)

print(values[:3])
