📂 File Organizer

A smart and lightweight Python script to list, sort, and organize files by type in any folder.
Perfect for tidying up messy directories, categorizing projects, or finding what you need—fast ⚡

✨ Features

List or sort files by type: images, documents, spreadsheets, presentations, audio, video, archives, code, misc, or all.

Recursive search through subfolders 🔍

Flexible: specify any folder with a command-line flag.

Lightweight and Pythonic — no heavy dependencies 🐍

Built-in test mode to quickly preview file detection 🧪

📁 Supported File Types

Images: jpg, jpeg, png, gif, bmp, tiff, webp
Documents: doc, docx, odt, pdf, txt, md, rtf
Spreadsheets: xls, xlsx, ods, csv
Presentations: ppt, pptx, odp
Audio: mp3, wav, aac, flac, ogg, m4a
Video: mp4, avi, mov, mkv, wmv, flv, webm
Archives: zip, tar, gz, rar, 7z, bz2
Code: py, c, cpp, h, java, js, ts, html, css, rb, go, rs, php, swift, sh
Misc: json, xml, yaml, yml, ini, cfg, log

…and more!

🚀 Usage
# List all files
python3 main.py list

# List files of a specific type
python3 main.py list images

# List files in a specific folder
python3 main.py list images -f /path/to/folder

# Sort (copy) files into organized folders
python3 main.py sort images

🧪 Test Function

You can run a quick test directly in Python:

from main import test_list
test_list()

❤️ Why You’ll Love It

Fast, minimal, and intuitive

Great for developers, creators, and anyone drowning in cluttered folders

Easy to extend — add new file types or logic in seconds

Turns chaos into calm, one neatly sorted directory at a time