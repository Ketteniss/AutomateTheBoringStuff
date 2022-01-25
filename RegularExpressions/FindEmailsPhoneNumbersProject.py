import pyperclip, re
# get text off the clipboard
text = str(pyperclip.paste())

# search text

# regex1: phonenumber
regexPhoneNum = re.compile(r"""(
    (\d{3}|\(\d{3\))?               # area code
    (\s|-|\.)?                      # seperator
    (\d{3})                         # first 3 digits
    (\s|-|\.)?                      # seperator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )""", re.VERBOSE)

# regex2: email 
regexEmail = re.compile(r"""(
    [a-zA-Z0-9._%+-]+   # username 
    @                   # @ SYMBOL
    [a-zA-Z0-9.-]+      # domain name 
    (\.[a-zA-Z]{2,4})   # dot-something   
    )""", re.VERBOSE)


# use regexes to find all matches
matches = []
for groups in regexPhoneNum.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in regexEmail.findall(text):
    matches.append(groups[0])

# format result into one string
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
