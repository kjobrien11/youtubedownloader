from __future__ import unicode_literals
import yt_dlp as youtube_dl
import ffmpy
import os
import argparse
import PySimpleGUI as sg


layout = [
      [sg.Text('Youtube Downloader')],
      [sg.Text('Youtube URl:', size=(20, 1)), sg.InputText()],
      [sg.Text('Output File Name:', size=(20, 1)), sg.InputText()],
      [sg.Submit(), sg.Cancel()]]

window = sg.Window('PictureSync', layout)

event, values = window.read()
window.close()


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--i', type=str, required=True)
parser.add_argument('-o', '--o', type=str, required=True)

args = parser.parse_args()

i = "temporaryname123.webm"

ydl_opts = {'outtmpl': i}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([args.i])

os.system(f"ffmpeg -i {i} {args.o}")
os.system(f"rm {i}")