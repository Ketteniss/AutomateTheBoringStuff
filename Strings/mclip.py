#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'Mamo': """23538428""",
        'vk1': """+491721687391""",
        'vk2': """loGR^EZ110Gr"""}

import sys
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase
import pyperclip
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase) 