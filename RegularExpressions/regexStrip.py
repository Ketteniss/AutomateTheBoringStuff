import re

def strip(string):

    # Write regex for string with leading or trailing white space
    regexLeading = re.compile(r'^(\s*)')
    regexTrailing = re.compile(r'(\s*)$')
    # Use re.sub() to substitute possible white space with empty string
    stripped = regexTrailing.sub('', regexLeading.sub('', string))
    print(f"'{stripped}'")
    return stripped
string = """
  sefesfesf esfesf werfwef sss eee


     
"""
strip(string)