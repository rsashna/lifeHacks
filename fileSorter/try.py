import os, glob, subprocess

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
| csv            | 'export*'        | exportCSVs    | --                             | --    |

Location Use Cases
-desktop -> screenshots
-downloads -> imgs, pdf, zip


FutureCase-ask to move to common locations?
FutureCase-Log file to track?
    -datestamp
    -ls -p > .fileSorterLog.txt
    --sort--
    -ls -p > .fileSorterLog.txt
    
"""



print("program started\n\n")
# Works ---v---
os.system("ls")

# Works --v-- lists header info
# subprocess.run(["ls", "-l"])

# Works ---v---
# subprocess.run(["ls"])


print("program ended\n\n")
