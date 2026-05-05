# Python Program to Find Factorial of Number Using Recursion
def fact(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * fact(n-1)

# input
n = int(input("Enter number: "))

print("Factorial =", fact(n))
