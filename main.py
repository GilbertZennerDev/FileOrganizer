"""this program will help you organize the files in your folder
allow the user to list all files of type 'x'
"""

from pathlib import Path

def list_filetype(rootfolder, gtype, *ty):
    images = ['*.jpg', '*.png']
    docs = ['*.odt', '*.doc', '*.md']
    if gtype == 'images': ty = images
    if gtype == 'docs': ty = docs
    root = Path(rootfolder)
    for t in ty:
        files = root.rglob(t)
        for file in files: print(file.resolve())

list_filetype('.', 'images')
print('='*30)
list_filetype('.', 'docs', '*.py', '*.c', '*.md')
print('='*30)
#list_filetype('testfiles', 'all', '*.py', '*.c', '*.md')
print('='*30)