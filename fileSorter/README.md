## Creating fileFormatter.csv

#### Sample fileFormatter

```
FileType,Pattern,FolderName,Rename,SpecialINST
x,Screen\ Shot*,screenshotsToMove,y,
jpg,x,imgsToMove,y,
jpeg,x,imgsToMove,y,
pdf,x,docsToMove,y,
x,export,csvExports,n,
```

* To leave fields blank, use 'x' only
* Rename column must be y or n

### Location
* place fileFormatter.csv where files are
  * subdirectories will be created here to move files
