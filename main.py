from __future__ import unicode_literals
import yt_dlp as youtube_dl
import ffmpy
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--i', type=str, required=True)
parser.add_argument('-o', '--o', type=str, required=True)

args = parser.parse_args()

i = "temporaryname123.webm"

ydl_opts = {'outtmpl': 'temporaryname123.webm'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([args.i])

os.system(f"ffmpeg -i {i} {args.o}")
os.system(f"rm {i}")