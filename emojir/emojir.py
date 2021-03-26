#!/usr/bin/python

import pandas as pd

face = input("Emoji type, or r=regularShrug: ")

if face == 'r':
    emoji = "¯\_(ツ)_/¯"
else:
    emoji = "¯\_("+ face +")_/¯"

df=pd.DataFrame([emoji])
df.to_clipboard(index=False,header=False)

print("Copied " + emoji)
