import re

stringy="""Postman Pat - intro theme - 1981 version  (closed captions) by\
cartooninpictures 12 years ago 1 minute, 32 seconds 1,124,265 views"""

timesec=re.search("years ago ([0-9]) [a-zA-Z]{0,}, ([0-9]{0,})", stringy)

print(timesec.group(1))
print(timesec.group(2))

timemin=int(timesec.group(1))
timesec=int(timesec.group(2))

timetot=timemin*60+timesec
print(timetot)
