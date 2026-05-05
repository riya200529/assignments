# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead If the string length of the given
# string is less than 3, leave it unchanged
s = input("Enter a string: ")

if len(s) < 3:
    result = s
elif s.endswith("ing"):
    result = s + "ly"
else:
    result = s + "ing"

print(result)
