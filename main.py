# import modules
from pytube import YouTube
import ffmpeg

# input music's info
title = input(' Input music\'s title : ')
artist = input(' Input artist\'s name : ')
link = input(' Input music\'s YouTube URL : ')

# download video from YouTube
yt = YouTube(link)
yt.streams.filter(only_audio=True).first().download()

# convert mp4 file to mp3
input = ffmpeg.input(f'{yt.streams.filter(only_audio=True).first().download()}')
audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
out = ffmpeg.output(audio, f'{title} - {artist}.mp3')
ffmpeg.run(out)