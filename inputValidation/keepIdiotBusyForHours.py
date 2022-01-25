import pyinputplus as pyip
# simple program using PyInputPlus Modul to ask yes or no questions

while True:
    prompt = 'Want to know how to keep an idiot up for hours?\n'
    askFool = pyip.inputYesNo(prompt)
    if askFool == 'no':
        print('Good day, sir!')
        break