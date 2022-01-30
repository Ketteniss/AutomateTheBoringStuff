#!python3
# findSpaceyFiles.py - Small program to find and list all files over 100mb
#                      inside specified src dir and list them in the console
import sys, os, shutil
from pathlib import Path

def main(src):
    # Go through src tree and check every file's size
    for foldername, subfolders, filenames in os.walk(src):
         for filename in filenames:
            try: 
                if not os.path.getsize(Path(foldername) / filename) > 100000000:
                    continue
                print(Path(foldername) / filename)
            except:
                pass
    # If Size is over 100mb print filename

main(sys.argv[1])