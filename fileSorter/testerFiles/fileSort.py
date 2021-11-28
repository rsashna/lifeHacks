import os, glob, subprocess
import pandas as pd
import numpy as np
# TODEL 1
from PIL import Image

# import matplotlib.pyplot as plt
import cv2

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
| xlsx           |--                | excelSheets    |                                |          |
| dmg           |--                | dontNeedButKeep    |                                |          |
| ics           |--                | --                 |                                |          |
| ~           |--                | --                 |                                |  delete these files        |


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
gohome = 'n'
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
    # print(toRename)
    if(toRename=='y'):
        renamer.append(folderToSend)
        # pd.concat([renamer,folderToSend])
        # print(renamer.dtype)
        # print(folderToSend.dtype)

    # TODEL check read_csv
    # print('typeOfFile pattern folderToSend\n', typeOfFile, pattern, folderToSend)


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

    # BUG not working
    if (pattern=='x'):
        command = ('mv *.' + typeOfFile  + ' ./' + folderToSend)
        # print(command)

    else:
        command = ('mv ' + pattern  + ' ./' + folderToSend)
        # print('CHECK')
        # print(command)
        # good to go for else
    os.system(command)

# itterate through renamer, ask to rename contents of i folder, if y
# go inside dir, take list into array, intterate through list, ask to rename, if y show img
# TODO - check if img files present, then show img
renamer=list(set(renamer))
# TODEL 1
print("\n\n renamer list:" , renamer)

for i in range (0,len(renamer)):
    print("\nRename files from " , renamer[i], "? [y/n]")
    if(gohome == 'y'):
        os.chdir('..')
    agreeRe = input("")
    if (agreeRe=="y"):
        cwd = os.getcwd()
        command = (cwd + '/' + renamer[i] + '/')
        # print(command , "now go inside folder")
        # TODEL 1
        print("Going into" + command)
        os.chdir(command)
        gohome = 'y'
        # TODEL 3
        # print('listing cont: ')
        # command = ('ls -a')
        # os.system(command)
        fileList = os.listdir(path='.')
        # print("FILE LIST" , fileList)
        for i in range (0,len(fileList)):
            print("\nShow " , fileList[i], "? [y/n]")
            agreeSh = input("")
            if (agreeSh=="y"):
                img=cv2.imread(fileList[i])
                # must focus on new img window and press any key to close img
                if img is None:
                    sys.exit("Could not read the image.")

                cv2.imshow("Rename this file", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.waitKey(1)
            # else:
                # dont show it
            print("\nRename " , fileList[i], "? [y/n]")
            agreeReFile = input("")
            if (agreeReFile=="y"):
                print("\nENTER NEW NAME FOR " , fileList[i], ":")
                orgName, fExt = os.path.splitext(fileList[i])
                newName = input("")
                newName = newName + fExt
                os.rename(fileList[i],newName)





# TODO: if pattern exists, list pattern.filetype > fileMoverAr ---DONE, just need to cleanup/uncomment
# TODO: make formatter files hidden --LAST STEP
# TODO: ask to rename **Might move this to process end
cv2.destroyAllWindows()
elapsed = time.time() - t
print("\n\n\n" + str(elapsed) + "s\nprogram ended\n\n")
