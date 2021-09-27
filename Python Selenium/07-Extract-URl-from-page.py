#!/usr/bin/python3
import re , linkGrabber
links = linkGrabber.Links("https://www.google.com")
gb = links.find(limit=8,duplicates=False,pretty=True)
for g in gb:
    print(g)