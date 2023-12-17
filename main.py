# import modules
from pytube import YouTube
import ffmpeg
import eyed3
print('Modules ready!')

# infomation
print('''
__   __               _____         _                               _____  ______                          _                    _             
\ \ / /              |_   _|       | |                             |____ | |  _  \                        | |                  | |            
 \ V /   ___   _   _   | |   _   _ | |__    ___   _ __ ___   _ __      / / | | | |  ___  __      __ _ __  | |  ___    __ _   __| |  ___  _ __ 
  \ /   / _ \ | | | |  | |  | | | || '_ \  / _ \ | '_ ` _ \ | '_ \     \ \ | | | | / _ \ \ \ /\ / /| '_ \ | | / _ \  / _` | / _` | / _ \| '__|
  | |  | (_) || |_| |  | |  | |_| || |_) ||  __/ | | | | | || |_) |.___/ / | |/ / | (_) | \ V  V / | | | || || (_) || (_| || (_| ||  __/| |   
  \_/   \___/  \__,_|  \_/   \__,_||_.__/  \___| |_| |_| |_|| .__/ \____/  |___/   \___/   \_/\_/  |_| |_||_| \___/  \__,_| \__,_| \___||_|   
                                                            | |                                                                               
                                                            |_|                                                                               

''')
print('Made by KeyFrog')

# input music's info
title = input(' Input music\'s title : ')
artist = input(' Input artist\'s name : ')
album = input(' Input album\'s name : ')
link = input(' Input music\'s YouTube URL : ')

# download video from YouTube
yt = YouTube(link)
yt.streams.filter(only_audio=True).first().download()
print(' DOWNLOAD SUCCESS!')

# convert mp4 file to mp3
input = ffmpeg.input(f'{yt.streams.filter(only_audio=True).first().download()}')
audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
out = ffmpeg.output(audio, f'{title} - {artist}.mp3')
ffmpeg.run(out)
print(' CONVERT SUCCESS!')

# add metadata
audiofile = eyed3.load(f"{title} - {artist}.mp3")
audiofile.tag.artist = artist
audiofile.tag.album = album
audiofile.tag.title = title
audiofile.tag.save()
print(' ADD METADATA SUCCESS')