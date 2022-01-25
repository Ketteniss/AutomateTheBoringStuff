import re, pyperclip
text = pyperclip.paste()
regexDate = re.compile(r'((0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/([1-2][0-9]{3}))')
matches = []
for group in regexDate.findall(text):
    day, month, year = group[1], group[2], group[3]
    matches.append([day, month, year])  
for i in range(len(matches)):
    if int(matches[i][1]) in range(4,12,2):
        if int(matches[i][0]) > 30:
            del matches[i]
    # February
    elif int(matches[i][1]) == 2:
        
        # Leap year?                  
        if (int(matches[i][2]) % 4) == 0:
            print(True)
            if not (int(matches[i][2]) % 100) == 0:
                if int(matches[i][0]) > 29:
                        del matches[i]
            elif (int(matches[i][2]) % 400) == 0:
                    if int(matches[i][0]) > 29:
                        del matches[i]
        else:
            
            if int(matches[i][0]) > 28:
                
                del matches[i] 
print(matches)
# 28/02/2001