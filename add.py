#!/usr/bin/python3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, COMM
filename = input("Path to file: ")
aid = input("Artist ID: ")

try:
    tags = ID3(filename)
except ID3NoHeaderError:
    tags = ID3()

tags["COMM"] = COMM(encoding=3, lang=u'eng', desc='desc', text="a"+str(aid))

# TODO: Insert function to check sanity of user against database

tags.save(filename)
