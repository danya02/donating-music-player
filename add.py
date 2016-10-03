#!/usr/bin/python3
import mutagen
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC
filename = input("Path to file: ")
aid = input("Artist ID: ")

try:
    tags = ID3(filename)
except ID3NoHeaderError:
    tags = ID3()

tags["COMM"] = COMM(encoding=3, lang=u'eng', desc='desc', text="a"+str(aid))

# TODO: Insert function to check sanity of user against database

tags.save(filename)
