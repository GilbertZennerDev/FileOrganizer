🗂️ File Organizer CLI

A simple Python tool to list, sort, and compress files by type — straight from your terminal.
Built for people who like clean folders and clean code.

🚀 Features

List files by type — e.g. images, docs, video, code, or all.

Sort files automatically into categorized folders.

Find duplicates using file checksums (SHA-256).

Search by name fragment across file types.

Compress / decompress folders or files (.zip support).

⚙️ Usage
python3 main.py <command> [options]

Commands
Command	Description
list	List all files of a given type
sort	Copy all files of a given type into a subfolder (test/<type>)
piece <text>	List files containing <text> in their name
duplicate	Detect duplicate files based on checksum
compress <folder>	Compress a folder into a .zip
decompress <archive>	Extract a .zip archive
💡 Examples

List all images in the current directory:

python3 main.py list images


Sort all code files into test/code/:

python3 main.py sort code


Find all files with “report” in their name:

python3 main.py piece report


Detect duplicates in your folder:

python3 main.py duplicate


Compress a folder:

python3 main.py compress ./my_project

🧩 Supported File Types

Images: jpg, png, gif, bmp, webp
Docs: pdf, docx, txt, md, rtf
Sheets: xls, xlsx, csv
Audio: mp3, wav, flac
Video: mp4, mkv, mov
Code: py, cpp, js, html, css, etc.
…and more.

🧠 Requirements

Python ≥ 3.7

Works cross-platform (Linux, macOS, Windows with PowerShell)

🛠️ Example Output
$ python3 main.py list docs
relative path: ./reports/summary.pdf
relative path: ./notes/todo.txt

⚡ Author

Made by someone who got tired of staring at messy folders.
Use it, tweak it, break it — just keep your workspace clean.
