#! python3
# strong_pw.py - Use regex to determine if password if good or nah

import re

while True:

    pw = input("Please enter your password: ")

    charRegex = re.compile(r'\w{8,}')
    lowerRegex = re.compile(r'[a-z]')
    upperRegex = re.compile(r'[A-Z]')
    numRegex = re.compile(r'\d{1,}')

    if charRegex.search(pw) is None:
        print("Passwords must be at least 8 characters.")
    elif lowerRegex.search(pw) is None:
        print("Passwords must contain lowercase characters.")
    elif upperRegex.search(pw) is None:
        print("Passwords must contain uppercase characters.")
    elif numRegex.search(pw) is None:
        print("Passwords must contain at least one digit.")
    else:
        print("Valid password found!")
        break
        
        
