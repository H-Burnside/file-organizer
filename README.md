# 🗂️ SIMPLE FILE ORGANIZER  
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A simple python script which helps you to automatically organize your files in folders for type (IMG, VIDEOS, DOCS, AUDIO)

## FEATURES
- **Automatic organization** - Classifies files by type 
- **Recursive searching** - It process subfolders
- **Secure** - It doesn't delete files, only move them
- **Fast** - It uses `os.scandir()` for an efficient iteration
- **Customizable** - Easy to modify and add categories

## USAGE
### INSTALLATION
```bash
git clone https://github.com/H-Burnside/file-organizer.git
cd file-organizer
```
### BASIC USAGE
```bash
python main.py /folder/to/organize
```

### EXAMPLE
How to organize Downloads 

- Linux
```bash
python main.py ~/Downloads
```
- Windows
```bash
python main.py C:\Users\YourName\Downloads
```

## CONFIGURATION
```python
extensions = {
    "images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico"
    ],
    "documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt",
        ".xls", ".xlsx", ".ppt", ".pptx", ".csv"
    ],
    "video": [
        ".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm", ".m4v"
    ],
    "audio": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"
    ],
    "archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"
    ],
    "executables": [
        ".exe", ".msi", ".bat", ".sh", ".bin", ".app", ".run"
    ],
    "packages": [
        ".deb", ".rpm", ".apk", ".snap", ".flatpak"
    ],
    "code": [
        ".py", ".c", ".cpp", ".h", ".hpp", ".js", ".ts",
        ".java", ".cs", ".html", ".css", ".json", ".xml", ".yaml", ".yml"
    ],
    "databases": [
        ".db", ".sqlite", ".sql"
    ],
    "fonts": [
        ".ttf", ".otf", ".woff", ".woff2"
    ],
    "disk_images": [
        ".iso", ".img"
    ]
}
```

### ADVANCED CONFIGURATION
MAXDEPTH = 10   # MAX SEARCH DEPTH

## PROJECT STRUCTURE
file-organizer/<br>
|<br>
|---main.py     # Main script<br>
|---README.md   # Documentation<br>
|---LICENSE     # Licence<br>

## DISCLAIMER
Files with unknown or non-existent extension will not be moved by the script, for added security you can do a backup of your data before the action. Remember: the script **MOVE** files, it doesn't copy the files.

## CONTRIBUTE
Just with sharing you're doing a great job.

## LICENSE
This project is covered by the MIT LICENSE

## AUTHOR
[![GitHub](https://img.shields.io/badge/GitHub-H--Burnside-blue?logo=github)](https://github.com/H-Burnside)
