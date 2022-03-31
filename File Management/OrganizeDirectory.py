import os
from pathlib import Path
DirectoryType={
        "DOCUMENTS": ['.pdf','.txt'],
        "AUDIO": ['.mp3','.m4a'],
        "VIDEO":['.mp4','.mov'],
        "IMAGES":['.jpg','.png','.jpeg']
    }
# c is category and s is suffix
def pickDirectory(value):
    for c,s in DirectoryType.items():
        for stemp in s:
            if stemp==value:
                return c
    return 'MISC'    

#scandir in OS library will grad each and every object of dir and files extension
#to get the path of each item we use PATHLIB and import Path module
#.suffix returns the file extension
def organizeDir():

    for files in os.scandir():
        if files.is_dir():
            continue
        filePath=Path(files)
        filetype=filePath.suffix.lower()
        directory=pickDirectory(filetype) #calling method
        directoryPath=Path(directory)
       
        #if directoryPath.is_dir()!=True:
            #directoryPath.mkdir() 

        filePath.rename(directoryPath.joinpath(filePath)) # adding Dir to file path to move it
        
organizeDir()
        



