import os
from pathlib import Path
os.chdir(Path.home())
totalSize = 0
for filename in os.listdir(Path.home()):
    print (filename)
    totalSize += os.path.getsize(os.path.join(Path.home(),filename))
    print(os.path.getsize(filename))
print(totalSize)