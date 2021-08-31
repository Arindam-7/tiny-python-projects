#! /usr/bin/env python3

#contactSearch.py - Extracts phone number and email address from the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\+\d\d)?  #area code
    (\s|-)?  #seperator
    (\d{10})  #last ten numbers
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  #username
    @  # @ symbol
    [a-zA-Z0-9.+]+  #domain name
    (\.[a-zA-Z]{2,4}){1,2}  # dot something
)''', re.VERBOSE)


text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = ''.join([groups[1], groups[3]])
    # print('First group', groups[1])
    # print('Second group', groups[2])
    # print('Third group', groups[3])
    # print('Phone Number = ', phoneNum)

    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


if len(matches) > 0:
    output = '\n'.join(matches)
    pyperclip.copy(output)
    print('Output copied to clipboard.')
    print('Output is - \n' + output)
else:
    print('No phone number or email addresses found.')

