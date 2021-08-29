#! /usr/bin/env python3

# This is just a small password manager

passwords = {
    'email': 'euvewyurvryryr47r7493ur',
    'hotstar': '4736483ff',
    'netflix': 'fh8efe7432rbf3yr39'
}


import sys
import pyperclip

if len(sys.argv)<2:
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print("Password is not saved for " + account)

