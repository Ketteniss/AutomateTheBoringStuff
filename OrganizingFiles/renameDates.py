# Program should:
    # Search all filenames in the cwd for american style dates
    # When one is found, rename with month and day swapped (to make european style)
    
    # To accomplish the goal the code should:
        # Create regex that identifies american style dates
        # Call os.listdir() to find all file in cwd
        # Loop over filenames, check each with regex
        # If regex encounters a hit, rename file with shutil.move()

#!python3
# renameDates.py - Rename files: American style (MM-DD-YYYY) to European (DD-MM-YYYY)

import os, re, shutil
from pathlib import Path

# american style
regexAmeDates = re.compile(r"""^(.*?)   # Text before
                    ((0|1)?\d)          # Month
                    -                   # Sep
                    ((0|1|2|3)?\d)      # Days
                    -                   # Sep
                    ((19|20)\d\d)       # Years
                    (.*?)$              # Text after
                    """, re.VERBOSE)
    
# Loop over the files in the working directory.
for file in os.listdir():
    moAmeDates = regexAmeDates.search(file)
    # Skip files without a date.
    if moAmeDates == None:
        continue
    # Get the different parts of the filename.    
    
    before, after = moAmeDates.group(1), moAmeDates.group(8)
    month, days, years = moAmeDates.group(2), moAmeDates.group(4), moAmeDates.group(6)

    # Form the European-style filename.
    euroDateFileName = f'{before}{days}-{month}-{years}{after}'

    # Get the full, absolute file paths.
    fullabsPath = Path.cwd() / file
    # Rename the files.
    #shutil.move(fullabsPath, Path.cwd() / euroDateFileName)
    print(f'{fullabsPath} to {Path.cwd() / euroDateFileName}')