# Mini project :
# Problem Statement : Password Generator
# Make a program to generate a strong password using the input given by the user. To generate a password,
# randomly take some words from the user input and then include numbers, special characters and capital
# letters to generate the password. Also, keep a check that password length is more than 8 characters.
# Note: Include Exception handling wherever required. Also, make a ‘User’ class and store the details like user
# id, name and password of each user as a tuple. 

def make_password(text):
    words = text.split()
    
    pwd = words[0] + words[1] + "12@"  
    
    if len(pwd) < 8:
        pwd = pwd + "123"         
        
    return pwd.capitalize()

class User:
    def __init__(self, i, n, p):
        self.data = (i, n, p)


try:
    i = int(input("Enter id: "))
    n = input("Enter name: ")
    text = input("Enter words: ")

    p = make_password(text)

    u = User(i, n, p)

    print("Password:", p)
    print("User data:", u.data)

except:
    print("Error")