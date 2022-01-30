#!python
# fillGaps.py - Fill or insert gaps in an ordered list of filenames

import os, sys, re, shutil      
from pathlib import Path         

print(sys.argv)

def main(pref, src, mode = 'fill'):    
    
    # Regex to indentify ordering
    regexOrdering = re.compile(r"""
    
    (\d+)
    
    """, re.VERBOSE)

    # Group all files with a shared prefix
    fileNameInfo = []
    upperBound = 0
    for file in os.listdir(src):
        if not pref in file:
            continue
        position = int(regexOrdering.search(file).group())
        if position > upperBound: upperBound = position
        fileNameInfo.append((file, position))
        
    # Max number of digits in ordering
    digitMax = len(str(len(fileNameInfo)))

    if mode == 'fill':
        # Traverse ordering bottom upwards, correcting gaps on the way up
        for posInNewOrder in range(1, len(fileNameInfo) + 1):
            # Identify lowest ordered file
            lowestInOldOrder = upperBound
            for i in range(len(fileNameInfo)):
                if fileNameInfo[i][1] < lowestInOldOrder:
                    lowestInOldOrder = fileNameInfo[i][1]
                    indexOfLowest = i 
            oldFileName = fileNameInfo.pop(indexOfLowest)[0]

            # Correct gap if existent
            if lowestInOldOrder > posInNewOrder:
                newPosition = '0'*(digitMax - len(str(posInNewOrder)) + 1) + str(posInNewOrder)
                newFileName = regexOrdering.sub(newPosition, oldFileName)
                oldPath = Path(src) / oldFileName
                newPath = Path(src) / newFileName
                shutil.move(oldPath, newPath)
                #print(oldPath)
                #print(newPath)
        
    if mode == 'insert':
        # Adjust the ordering so that the gap specified emerges
        pass

main(sys.argv[1], sys.argv[2])
