📂 File Organizer

A simple and smart Python script to list and organize files by type in any folder. Perfect for tidying up messy directories and quickly finding what you need! ⚡

Features ✨

List files by type: images, documents, spreadsheets, presentations, audio, video, archives, code, misc, or all.

Supports recursive search in subfolders. 🔍

Flexible: specify any folder with a command-line flag.

Lightweight and Pythonic—no heavy dependencies required. 🐍

Built-in test function to quickly check different file types. 🧪

Supported File Types 📁

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

Usage 🚀
# List all files
python3 main.py list

# List specific type
python3 main.py list images

# List files in a specific folder
python3 main.py list images -f /path/to/folder

Test Function 🧪

Quickly test file listing:

from main import test_list
test_list()

Why You'll Love It ❤️

Fast, lightweight, and easy to extend

Perfect for developers, content creators, and anyone with a messy folder

Makes organizing and finding files a breeze