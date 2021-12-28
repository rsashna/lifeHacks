import os, glob, subprocess
import pandas as pd
import numpy as np
# TODEL 1
# from PIL import Image

# import matplotlib.pyplot as plt
import cv2

import time

"""
Summary of working parts
-rename works
-file move works
-file delete after request works
-move back to current location
-patched: new show file command loop (doesnt reach)
-zipped file will be deleted if folder with same name exists

Not working
-ah ha bug, printing of movement folder when already exists?
-zips
    -special inst?
    -Should prog first show content before deleting???
-random z folder being created?
    -should zips be sent there or deleted???



PROCESS

scan in hidden file formater from same location (.fileformatter.txt)
    extract file structure (1)

-from the formatter create folders if they dont exist
-batch sort into folder using pattern or fileType
    -ask to rename or delete file
        -if y
        -for each file,
            -ask to show file
            -ask to rename
            -rename
-for zip files, look for duplicate named folder
    -if duplicate, delete zip
    -ask to rename folder


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

***FutureCase-Log file to track?
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
    # BUG - Some error message printing out... related to glob?
    print("AH HA")

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

    elif (pattern!='z'):
        command = ('mv ' + pattern  + ' ./' + folderToSend)
        # print('CHECK')
        # print(command)
        # good to go for else
    os.system(command)


    # zip file handling
    # look for all zips
    # -for zip files, look for duplicate named folder
    #     -if duplicate, delete zip
    #     -ask to rename folder
    if( pattern =='z'):
        # pattern z indicates zipped file pattern
        # zipped file will be deleted if folder with same name exists
        allZips=glob.glob('*.zip')
        # TODEL 2
        # print(allZips)
        # print("CHECK - QUIT PROG")
        for z in range(0,len(allZips)):
            zipName, zExt = os.path.splitext(allZips[z])
            zipFolder=zipName + '/'
            if (glob.glob(zipFolder)!=[]):
                print("Found a folder and a zipped file named" , zipName)
                print("Zip being deleted: " , zipName)
                command = ('mv ' + allZips[z] + ' ~/.Trash/')
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
            orgName, fExt = os.path.splitext(fileList[i])
            fExt=fExt.lower()
            mediaType = 0
            # check if img 1, doc 2, vid 3, aud 4
            if (fExt==".png" or fExt==".jpg" or fExt==".jpeg" or fExt==".tiff" or fExt==".gif" or fExt==".heic" ):
                mediaType = 1
            elif(fExt==".pdf" or fExt==".docx"):
                mediaType = 2
            elif(fExt==".mov" or fExt==".mp4"):
                mediaType = 3
            elif(fExt==".wav" or fExt==".m4a"):
                mediaType = 4

            # should handle all accepted file types
            # prompt and execute, files to be shown/renamed/deleted
            if (agreeSh=="y" and mediaType!=0):
                command = ('open -R ' + fileList[i])
                print("\nOpening in finder. Close window then continue here.")
                os.system(command)

            print("\nRename or Delete" , fileList[i], "? [r/d/n]")
            agreeModFile = input("")
            if (agreeModFile=="r"):
                print("\nENTER NEW NAME FOR " , fileList[i], ":")

                newName = input("")
                newName = newName + fExt
                os.rename(fileList[i],newName)
            elif (agreeModFile=="d"):
                print("\nMoving " , fileList[i], " to Trash.")
                command = ('mv ' + fileList[i] + ' ~/.Trash/')
                os.system(command)



# TODO: if pattern exists, list pattern.filetype > fileMoverAr ---DONE, just need to cleanup/uncomment
# TODO: make formatter files hidden --LAST STEP
# TODO: ask to rename **Might move this to process end
cv2.destroyAllWindows()
elapsed = time.time() - t
print("\n\n\n" + str(elapsed) + "s\nprogram ended\n\n")
