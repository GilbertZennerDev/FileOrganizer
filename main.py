"""
this program will help you organize the files in your folder
allow the user to list all files of type 'x'
"""

import sys
import subprocess as sp
from pathlib import Path
import hashlib
import shutil

def get_pure_filename(total_name):
    total_name = str(total_name)
    while '/' in total_name:
        total_name = total_name[total_name.index('/') + 1:]
    return total_name

def all_types(what):
    # Image files
    images = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff', '*.webp']

    # Document files
    docs = ['*.doc', '*.docx', '*.odt', '*.pdf', '*.txt', '*.md', '*.rtf']

    # Spreadsheet files
    sheets = ['*.xls', '*.xlsx', '*.ods', '*.csv']

    # Presentation files
    presentations = ['*.ppt', '*.pptx', '*.odp']

    # Audio files
    audio = ['*.mp3', '*.wav', '*.aac', '*.flac', '*.ogg', '*.m4a']

    # Video files
    video = ['*.mp4', '*.avi', '*.mov', '*.mkv', '*.wmv', '*.flv', '*.webm']

    # Archive / compressed files
    archives = ['*.zip', '*.tar', '*.gz', '*.rar', '*.7z', '*.bz2']

    # Code files (common programming languages)
    code = ['*.py', '*.c', '*.cpp', '*.h', '*.java', '*.js', '*.ts', '*.html', '*.css', '*.rb', '*.go', '*.rs', '*.php', '*.swift', '*.sh']

    # Misc / config / data files
    misc = ['*.json', '*.xml', '*.yaml', '*.yml', '*.ini', '*.cfg', '*.log']

    # Combine all into a single list if you want
    all_types = images + docs + sheets + presentations + audio + video + archives + code + misc

    if what == 'images': return images
    if what == 'docs': return docs
    if what == 'sheets': return sheets
    if what == 'presentations': return presentations
    if what == 'audio': return audio
    if what == 'video': return video
    if what == 'archives': return archives
    if what == 'code': return code
    if what == 'misc': return misc
    if what == 'all': return all_types
    return None

def getrelativepath(file):
    return str(Path(file.resolve()).relative_to(Path.cwd()))

def sort_filetype(rootfolder, gtype):
    root = Path(rootfolder)
    result = all_types(gtype)
    if result is None: exit()
    sp.run(['mkdir', '-p', f'test/{gtype}'])
    for t in result:
        for file in root.rglob(t):
            sp.run(f'cp -r {getrelativepath(file)} test/{gtype}', shell=True)

def list_filetype(rootfolder, gtype):
    root = Path(rootfolder)
    result = all_types(gtype)
    if result is None: exit()
    for t in result:
        for file in root.rglob(t): print(f"relative path: ./{getrelativepath(file)}")

def list_piece(rootfolder, gtype, piece):
    root = Path(rootfolder)
    result = all_types(gtype)
    if result is None: exit()
    for t in result:
        for file in root.rglob(t):
            rel_path = getrelativepath(file)
            name = get_pure_filename(rel_path)
            if piece in name:
                print(f"relative path: ./{getrelativepath(file)}")

def handle_list(what):
    list_cmds = ['images', 'docs', 'sheets', 'presentations', 'audio', 'video', 'archives', 'code', 'misc', 'all']
    print("Optional list commands:", list_cmds)
    folder = Path.cwd()
    types = 'all'
    if len(sys.argv) < 3: list_filetype(folder, 'all')
    elif len(sys.argv) == 3: types = sys.argv[2]
    else:
        if sys.argv[3] == '-f': folder = sys.argv[4];
    if what == 'list': list_filetype(folder, types)
    elif what == 'sort':  sort_filetype(folder, types)

def checksum(path, algo="sha256"):
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def find_checksum(allnames, searched_checksum):
    counter = 0
    hashednames = [checksum(name) for name in allnames]
    for cksum in hashednames:
        if cksum == searched_checksum: counter += 1
    return counter

def find_duplicates(rootfolder, gtype):
    root = Path(rootfolder)
    result = all_types(gtype)
    if result is None: exit()
    allnames = []
    for t in result:
        for file in root.rglob(t):
            allnames.append(str(getrelativepath(file)))
    allnames = set(allnames)
    print(allnames)
    for name in allnames:
        counter = find_checksum(allnames, checksum(name))
        if counter > 1: print(f"tmp: {name} exists {counter} times.")
        else: print(f"tmp: {name}  has no duplicates.")

def compress_file(filename):
    print("compressed", filename)
    shutil.make_archive(filename + '_compressed', "zip", root_dir=filename)

def decompress_file(filename):
    print("decompressed", filename)
    shutil.unpack_archive(filename, ".")

def test_list():
    list_filetype('.', 'images')
    print('='*30)
    list_filetype('.', 'docs')
    print('='*30)
    list_filetype('testfiles', 'all')
    print('='*30)

def main():
    cmds = ['list']
    ac = len(sys.argv)
    if ac < 2: print("Usage: python3 main.py", cmds); exit()
    if sys.argv[1] in 'listsort': handle_list(sys.argv[1])
    if sys.argv[1] in 'piece' and ac > 2:
            if ac > 3: list_piece('.', sys.argv[3], sys.argv[2])
            else: list_piece('.', 'all', sys.argv[2])
    if sys.argv[1] in 'duplicate': find_duplicates('.', 'all')
    if sys.argv[1] == 'compress' and ac >= 3: compress_file(sys.argv[2])
    if sys.argv[1] == 'decompress' and ac >= 3: decompress_file(sys.argv[2])

if __name__ == "__main__": main()