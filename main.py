"""this program will help you organize the files in your folder
allow the user to list all files of type 'x'
"""

from pathlib import Path
import sys

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

def list_filetype(rootfolder, gtype, *ty):
    root = Path(rootfolder)
    result = all_types(gtype)
    if result is None: exit()
    for t in all_types(gtype):
        files = root.rglob(t)
        for file in files: print(file.resolve())

def handle_list():
    list_cmds = ['images', 'docs', 'sheets', 'presentations', 'audio', 'video', 'archives', 'code', 'misc', 'all']
    print("Optional list commands:", list_cmds)
    if len(sys.argv) < 3: list_filetype('.', 'all')
    else:
        folder = '.'
        types = 'all'
        if len(sys.argv) >= 4 and sys.argv[3] == '-f': folder = sys.argv[4];
        types = sys.argv[2]
        list_filetype(folder, types)

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
    if sys.argv[1] == 'list': handle_list()

if __name__ == "__main__": main()