#Write a Python program to check whether a list contains a sublist.
main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4]

found = False

for i in range(len(main_list)):
    if main_list[i:i+len(sub_list)] == sub_list:
        found = True

print("Sublist found" if found else "Sublist not found")
