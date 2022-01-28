import re
from pathlib import Path

regexDB = re.compile(r'.*Regex.*')
fileObject = open(r'C:\Users\Default.DESKTOP-SBK9Q3H\OneDrive\VSC\Python\AutomateTheBoringStuff\ReadingWritingFiles\TestDirForRegexMatch\uhfinalllytxtyeay.txt', 'r')
for hit in regexDB.findall(fileObject.read()):
    print(hit)
fileObject.close()
