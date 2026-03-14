# file: file-organizer
# author: Henrry Burnside 

import os
import pathlib

destinydir = ''
sourcedir = ''
extensions = {
        "image": [".jpg",".jpeg",".png",".gif"],
        "doc": [".pdf",".docx",".txt",".xlsx"],
        "video": [".mp4",".mov",".avi",".mkv"],
        "audio": [".mp3",".wav"]
}

MAXDEPTH = 100

def movefiles(path):
    for file in listdir(path):
        with os.scandir(path) as files:
            for file in files:
                if file.is_dir:
                    movefiles(file)
                elif file.is_file:
                    pass

def movetodirectory(file):
    isAnRequiredFile = False
    extfile = file[os.extsep:]
    for ext in extensions.keys():
        if extfile in ext:
            isAnRequiredFile = True
            break
    if(isAnRequiredFile):
        destDir = f"{destinydir}{os.sep}{}"
        if(!pathlib.Path(destDir).exists):
            
    
