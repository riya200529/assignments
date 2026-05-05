# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if
# 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string
s = input("Enter a string: ")

if "not" in s and "poor" in s and s.index("not") < s.index("poor"):
    result = s.replace(s[s.index("not"): s.index("poor") + len("poor")], "good")
else:
    result = s

print(result)