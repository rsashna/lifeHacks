import os, glob, subprocess
import pandas as pd
import numpy as np

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

fileFormat = pd.read_csv('./fileFormatter.csv')

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
print('rows ' , ffrows)
print('cols ',ffcols)
print(fileFormat.iloc[0,2])
print(fileFormat.iloc[2,0])
print("NEXT")


# for each line in csv, if doesnt exist, create folderName
for i in range(0,ffrows):
    folderToSend = fileFormat.iloc[i,2]
    if (glob.glob(folderToSend)==[]):
        print('--CREATING FOLDER')
        command = 'mkdir ' + folderToSend
        print(folderToSend)
        os.system(command)

    #else:
        # dont make a folder

    typeOfFile = fileFormat.iloc[i,0]
    print(typeOfFile)
    print('check if nan')
    print(fileFormat.iloc[i,1])
    if (fileFormat.iloc[i,1]=='x'):
        print('found one')
        print(fileFormat.iloc[i,1])
        command = 'mv *.' + fileFormat.iloc[i,1] + './' + folderToSend
        print(command)

    # print(glob.glob(fileFormat.iloc[i,2]))




# TODO: if pattern exists, list pattern.filetype > fileMoverAr
# TODO: ask to rename **Might move this to process end

print("\n\n\nprogram ended\n\n")
