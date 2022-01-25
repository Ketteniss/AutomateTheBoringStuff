import re, sys
def strongPwCheck(password):
    regexUpper = re.compile(r'[A-Z]')
    regexLower = re.compile(r'[a-z]')
    regexDigit = re.compile(r'[0-9]')
    if len(password) < 8:
        print('Password too short')
        sys.exit()
    if regexDigit.search(password) == None:
        print('At least one digit')
        sys.exit()
    #print( regexDigit.search(password))
    if regexLower.search(password) == None:
        print('At least one lower-case letter')
        sys.exit()
    #print(regexLower.search(password))
    if regexUpper.search(password) == None:
        print('At least one upper-case letter')
        sys.exit()
    print('Strong!')
    #print(regexUpper.search(password))
pw = 'Verycool123'
strongPwCheck(pw)