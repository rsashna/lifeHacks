#!/usr/bin/python
# Image searcher which Ill be using to find memes :)

import webbrowser

kw = input("keyWords: ")
newkw = kw.replace(" ", "+")

# print("Your KW:" + newkw)

# format needed: https://www.google.com/search?q=cat+memes+crying&tbm=isch&ved
url = "https://www.google.com/search?q=" + newkw + "&tbm=isch&ved"

webbrowser.open_new_tab(url)

print(url + " opened in new tab")
