import sys, re
"""
if sys.argv < 2:
    print('Usage: python isPhoneNumber [argument] - argument must be a string')
    sys.exit()
if not isinstance(sys.argv[1], str):
    print('Error: Input must be string')
    sys.exit()"""

# A program to verify if a string as an argument
# is an american phone number

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return 
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False    
    return True

def isPhoneNumberRE(text):
    phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    if phoneNumberRegex.search(text):
        return True
    return False
    
print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print(isPhoneNumberRE('415-555-4242'))

print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))
print(isPhoneNumberRE('Moshi moshi'))