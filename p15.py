# Given a number n, write a python program to make and print the list of Fibonacci series up to n.
# Input : n=7
# Hint : first 7 numbers in the series
# Expected output :
# First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13
n = int(input("Enter n: "))

a = 0
b = 1

print("First few Fibonacci numbers are:")

for i in range(n + 1):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
