"""this program will help you organize the files in your folder
allow the user to list all files of type 'x'
"""

from pathlib import Path

def list_filetype(rootfolder = ".", *ty):
    root = Path(rootfolder)
    for t in ty:
        files = root.rglob(t)
        for file in files: print(file.resolve())

list_filetype('.', '*.py', '*.c', '*.md')
list_filetype('testfiles', '*.py', '*.c', '*.md')