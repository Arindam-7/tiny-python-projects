#! /usr/bin/env python3

#“A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.”

import re

def detector(password):
    numRegex = re.compile(r'[0-9]')
    uppercaseRegex = re.compile(r'[A-Z]')
    lowercaseRegex = re.compile(r'[a-z]')

    if len(password) < 8:
        return False
    elif not numRegex.search(password):
        return False
    elif not uppercaseRegex.search(password):
        return False
    elif not lowercaseRegex.search(password):
        return False
    else:
        return True

password = input("Enter Password: ")

if detector(password):
    print("Strong Password")
else:
    print("Make it strong, dude!")