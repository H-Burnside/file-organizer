# file: file-organizer
# author: Henrry Burnside 

import os

extensions = {
        "image": [".jpg",".jpeg",".png",".gif"],
        "doc": [".pdf",".docx",".txt",".xlsx"]],
        "video": [".mp4",".mov",".avi",".mkv"]],
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
                    
    

