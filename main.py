# file: file-organizer
# author: Henrry Burnside 

import os
import pathlib
import sys
import shutil

destinydir = sys.argv[1]

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

MAXDEPTH = 10
CURRENTDEPTH = 0

def movefiles(path):
    global CURRENTDEPTH
    if CURRENTDEPTH > MAXDEPTH:
        return

    with os.scandir(path) as files:
        for file in files:
            if file.is_dir():
                CURRENTDEPTH += 1 
                movefiles(file.path)
                CURRENTDEPTH -= 1
            elif file.is_file():
                movetodirectory(file.path)

def movetodirectory(file_path):
    file = pathlib.Path(file_path)

    extfile = file.suffix.lower()
    if not extfile:
        return
    
    category = None
    for cat, exts in extensions.items():
        if extfile in exts:
            category = cat
            break

    if category:
        destDir = pathlib.Path(f"{destinydir}/{category}")
        destDir.mkdir(exist_ok = True)
        
        destFile = f"{destDir}/{file.name}"

        # Moving the file
        shutil.move(str(file),str(destFile))
        print(f"{file} --> {destFile}")

movefiles(destinydir)
