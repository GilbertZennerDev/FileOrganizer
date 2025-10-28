lean"""this program will help you organize the files in your folder
allow the user to list all files of type 'x'
"""

import sys
import subprocess as sp
from pathlib import Path

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
    return Path(file.resolve()).relative_to(Path.cwd())

def sort_filetype(rootfolder, gtype, *ty):
    root = Path(rootfolder)
    result = all_types(gtype)
    if result is None: exit()
    sp.run(['mkdir', '-p', f'test/{gtype}'])
    for t in result:
        for file in root.rglob(t):
            sp.run(f'cp -r {getrelativepath(file)} test/{gtype}', shell=True)

def list_filetype(rootfolder, gtype, *ty):
    root = Path(rootfolder)
    result = all_types(gtype)
    if result is None: exit()
    for t in result:
        for file in root.rglob(t): print(f"relative path: ./{getrelativepath(file)}")

def handle_list(what):
    list_cmds = ['images', 'docs', 'sheets', 'presentations', 'audio', 'video', 'archives', 'code', 'misc', 'all']
    print("Optional list commands:", list_cmds)
    folder = Path.cwd()
    if len(sys.argv) < 3: list_filetype(folder, 'all')
    if len(sys.argv) > 3:
        if sys.argv[3] == '-f': folder = sys.argv[4];
        types = sys.argv[2]
        if what == 'list': list_filetype(folder, types)
        elif what == 'sort':  sort_filetype(folder, types)

def test_list():
    list_filetype('.', 'images')
    print('='*30)
    list_filetype('.', 'docs')
    print('='*30)
    list_filetype('testfiles', 'all')
    print('='*30)

def main():
    cmds = ['list']
    if len(sys.argv) < 2: print("Usage: python3 main.py", cmds); exit()
    if sys.argv[1] == 'list' or sys.argv[1] == 'sort': handle_list(sys.argv[1])

if __name__ == "__main__": main()