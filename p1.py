# Program to find the sum of first n positive integers

no = int(input("Enter a positive integer: "))
ans=0
for i in range(1,no+1):
    ans += i


print(f"Sum of the first positive integers is:{ans}" )
