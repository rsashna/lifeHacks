import os, glob, subprocess
import pandas as pd
import numpy as np
import time

"""
PROCESS

scan in hidden file formater from same location (.fileformatter.txt)
    extract file structure (1)

-for each file, sort into folder
-ask to rename screenshots
    -if y
    -for each ss,
        -show file, ask for name
        -rename


(1) General FILE FORMATTER (.fileformatter.txt)

| FileType       | Pattern          | FolderName    | SpecialINST                    | Notes    |
| png, jpeg, jpg | 'Screen Shot*'   | screenshots   | after sort ask to rename/trash |          |
| pdf            | --               | docsToMove    | after sort ask to rename/trash | --       |
| zips           | --               | zipsToMove    | FIRST check if folder exists with same name, if so, send to trashAfterSort/   |    |
| csv            | 'export*'        | exportCSVs    | --                             | --       |
| mov            |--                | screenRecs    |                                |          |


Location Use Cases
-desktop -> screenshots
-downloads -> imgs, pdf, zip


Feature-count the number of screen shots before move?
FutureCase-ask to move to common locations?
FutureCase-Log file to track?
    -datestamp
    -ls -p > .fileSorterLog.txt
    --sort--
    -ls -p > .fileSorterLog.txt


"""



print("program started\n\n")

t = time.time()

fileFormat = pd.read_csv('./fileFormatter.csv')
renamer = []

# Works ---v---
# os.system("ls")

# Works --v-- lists header info
# subprocess.run(["ls", "-l"])

# Works ---v---
# subprocess.run(["ls"])


# finds the screenshots
 # ls ./*Screen*.png | wc -l


# move to trash
# ~/.Trash/
[ffrows,ffcols] = fileFormat.shape
# TODEL test below:
# [ffrows,ffcols] = fileFormat.shape
# print('rows ' , ffrows)
# print('cols ',ffcols)
# print(fileFormat.iloc[0,2])
# print(fileFormat.iloc[2,0])
# print("NEXT")


# for each line in csv, if folder doesnt exist, create folder
for i in range(0,ffrows):
    typeOfFile = fileFormat.iloc[i,0]
    pattern = fileFormat.iloc[i,1]
    folderToSend = fileFormat.iloc[i,2]
    toRename = fileFormat.iloc[i,3]
    print(toRename)
    if(toRename=='y'):
        renamer.append(folderToSend)
        # pd.concat([renamer,folderToSend])
        # print(renamer.dtype)
        # print(folderToSend.dtype)

    # TODEL check read_csv
    print('typeOfFile pattern folderToSend\n', typeOfFile, pattern, folderToSend)


    if (glob.glob(folderToSend)==[]):
        print('\n--CREATING FOLDER')
        command = 'mkdir ' + folderToSend
        print(folderToSend)
        os.system(command)

    # else:
        # dont make a folder

    # move that file

    # TODEL check if no pattern
    # print(typeOfFile)
    # print('check if nan')


    if (pattern=='x'):
        command = ('mv *.' + typeOfFile  + ' ./' + folderToSend)
        print(command)

    else:
        command = ('mv ' + pattern  + ' ./' + folderToSend)
        print('CHECK')
        print(command)
        # good to go for both^
        # os.system(command)

# itterate through renamer, show img, ask to rename contents
renamer=list(set(renamer))
print(renamer)

# TODO: if pattern exists, list pattern.filetype > fileMoverAr ---DONE, just need to cleanup/uncomment
# TODO: make formatter files hidden --LAST STEP
# TODO: ask to rename **Might move this to process end

elapsed = time.time() - t
print("\n\n\n" + str(elapsed) + "s\nprogram ended\n\n")
