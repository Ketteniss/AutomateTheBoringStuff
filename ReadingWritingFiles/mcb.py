#! python3
# mcb.py - A (!)updatable multi-clipboard program.

import sys
import shelve 
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [arg_options][keyphrase] - arg_options: save, load or non')


shelfFile = shelve.open('keyphrase_data')

if len(sys.argv) == 3:
    # argv[1] => argument
    if sys.argv[1].lower() == 'save':
        print('hey there')
        shelfFile[sys.argv[2]] = pyperclip.paste()  

elif len(sys.argv) == 2:
    # argv[1] => argument
    if sys.argv[1].lower()  == 'list':
        pyperclip.copy(str(list(shelfFile.keys())))
    
    # argv[1] => keyphrase
    if sys.argv[1] in shelfFile:    
        pyperclip.copy(shelfFile[sys.argv[1]])
        print('Text for ' + sys.argv[1]  + ' copied to clipboard.')
    
    else:
        print('There is no text for ' + sys.argv[1] )

shelfFile.close()
sys.exit()