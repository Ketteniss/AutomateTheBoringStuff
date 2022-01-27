
#!python3
# A small programm that inserts USERTEXT for certain keyphrases

# modules?
#from pathlib import Path
import sys, re, pyinputplus as pyip

# set file path
filePath = sys.argv[1]
print(sys.argv[1])

# read text file
fileObject = open(filePath, 'r')
wholeText = fileObject.read()
Words = wholeText.split()

# regexes
reAdj = re.compile(r'ADJECTIVE')
reNoun = re.compile(r'NOUN')
reAdv = re.compile(r'ADVERB')
reVerb = re.compile(r'VERB')

for i in range(len(Words)):
    # get USERTEXT for specific phrases
    if 'ADJECTIVE' in Words[i]:
        adj = pyip.inputStr('Set ADJECTIVE: ')
        # substitue USERTEXT
        Words[i] = reAdj.sub(adj, Words[i])
    elif 'NOUN' in Words[i]:
        noun = pyip.inputStr('Set NOUN: ')
        # substitue USERTEXT
        Words[i] = reNoun.sub(noun, Words[i])
    elif 'ADVERB' in Words[i]:
        adv = pyip.inputStr('Set ADVERB: ')
        # substitue USERTEXT
        Words[i] = reAdv.sub(adv, Words[i])
    elif 'VERB' in Words[i]:
        verb = pyip.inputStr('Set VERB: ')
        # substitue USERTEXT
        Words[i] = reVerb.sub(verb, Words[i])

# reassemble string
new_string = ' '.join(Words)

# print new text in the command prompt
print(new_string)
fileObject.close()
