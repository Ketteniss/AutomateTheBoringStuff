#!python3
import webbrowser
import sys, logging, pyperclip
#logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main(arguments):

    if len(arguments) > 1:
        # Get address from command line
        address = ' '.join(sys.argv[1:])
    else:
        address = pyperclip.paste()
    webbrowser.open('https://www.google.com/maps/place/' + address)

main(sys.argv)