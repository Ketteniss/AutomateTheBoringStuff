import os, re, sys
from pathlib import Path
# General information @regexMatch_outline

def main (REGEX, DirToBeSearched, DirForResult):
    # Argument validation
    if len(sys.argv) < 4:
        print('Usage: python regexMatch.pyw [regex][search_path][result_path]\n')
        sys.exit()
    try:
        REGEX = re.compile(rf'{REGEX}')
    except re.error:
        print('Invalid arguments: Bad regex\n')
        sys.exit()
    if not os.path.isdir(sys.argv[2]) or not os.path.isdir(sys.argv[3]):
        print('Invalid arguments: Bad path\n')
        sys.exit()

                    # PREPARE SEARCH
    # Regex for .txt 
    regexTxt = re.compile(r'.*\.txt')
    # Make file list
    Dir = list(os.listdir(DirToBeSearched)) # possible improvement: Use Path objects
    # Hit count
    hits = 0
    # Open result file
    fileObject_result = open(Path(DirForResult) / 'result.txt', 'a') # possible improvement: Use Path objects

                    # SEARCH
    for file in Dir:
        if regexTxt.search(file) != None:
            fileObject = open(Path(DirToBeSearched) / file, 'r')
            for line in fileObject.readlines():
                if REGEX.search(line) != None:
                    hits += 1
                    # WRITE RESULT FILE
                    fileObject_result.write(f'{line}\n')
    fileObject.close()
    fileObject_result.close()

    # RETURN HITS
    return hits

print(main(sys.argv[1], sys.argv[2], sys.argv[3]))
