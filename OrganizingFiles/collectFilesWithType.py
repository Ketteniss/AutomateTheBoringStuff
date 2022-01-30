#!python3
# collectFilesWithType - Small program to search current 
# dirtree and copy all files found of specified type into 
# specified new folder


import sys, os, shutil
from pathlib import Path

def main(src, dst, ext):
    if not os.path.isabs(dst):
        print('Bad argument: Destination path needs to be absolute.')
        sys.exit()
    # Search src tree for every file with .fileEXT 
    for foldername, subfolder, filenames in os.walk(src):
        # Copy each file with the EXT into distination folder
        for filename in filenames:
            if not filename.endswith(f'.{ext}'):
                continue
            fileOrigin = Path(foldername) / filename
            fileDestination = Path(dst) / filename
            shutil.copyfile(fileOrigin, fileDestination)
            #print(fileOrigin, fileDestination)
    
   

main(sys.argv[1], sys.argv[2], sys.argv[3])
# Test: C:\Users\Default.DESKTOP-SBK9Q3H\OneDrive\VSC\Python>py C:\Users\Default.DESKTOP-SBK9Q3H\OneDrive\VSC\Python\AutomateTheBoringStuff\OrganizingFiles\collectFilesWithType.py C:\Users\Default.DESKTOP-SBK9Q3H\OneDrive\VSC\Python\AutomateTheBoringStuff\OrganizingFiles C:\Users\Default.DESKTOP-SBK9Q3H\OneDrive\VSC\Python\misc\CollectedTxt txt