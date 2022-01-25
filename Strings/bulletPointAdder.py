#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste().split('\r\n')
Tmp = []
for string in text:
    Tmp.append('%s\n' % (string))
text = '\r\n'.join(Tmp)
pyperclip.copy(text)
#print(text)