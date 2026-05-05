# Write a python program using function to find the sum of odd series and even series
# Odd series: 12/ 1! + 32/ 3! + 52/ 5!+……n
# Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n
# one factorial function
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

# main function
def series(n):
    odd = 0
    even = 0

    for i in range(1, n+1):
        if i % 2 == 0:
            even += (i*i) / fact(i)
        else:
            odd += (i*i) / fact(i)

    print("Odd series =", odd)
    print("Even series =", even)

# input
n = int(input("Enter n: "))
series(n)