# Write a Python program to find the second smallest number in a list. 
list1=[1,90,3,4,5,6,7,8,9,]
small=min(list1)
remove=list1.remove(small)
smallest=min(list1)
print(f"smallest number is: {smallest}")