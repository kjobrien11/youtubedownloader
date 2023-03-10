from __future__ import unicode_literals
import yt_dlp as youtube_dl
import ffmpy
import os
import argparse
import PySimpleGUI as sg


layout = [
      [sg.Text('Youtube URl:', size=(20, 1)), sg.InputText()],
      [sg.Text('Output File Name:', size=(20, 1)), sg.InputText()],
      [sg.Submit("Convert")]]

window = sg.Window('Youtube Video Downloader', layout)

event, values = window.read()
window.close()

i = "temporaryname123.webm"

ydl_opts = {'outtmpl': i}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([values[0]])

os.system(f"ffmpeg -i {i} {values[1]}")
os.system(f"rm {i}")