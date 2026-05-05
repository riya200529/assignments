#Write a Python program to get a single string from two given strings, separated by a space and swap the first
#two characters of each string. 
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")


new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]

result = new_s1 + " " + new_s2

print(result)
