from pytube import YouTube
import os

def download_audio():
    question = int(input('Аудио 1 или Видео 2 : '))
    video_url = input('Введите ссылку на видео с YouTube: ')
    yt = YouTube(video_url)
    name = f'{yt.streams[0].title}.mp3'
    namevid = f'{yt.streams[0].title}.mp4'
    if question == 1:
        try:
            #yt.streams.filter(only_audio=True).desc().first().download(filename=name)
            yt.streams.filter(type = "audio").first().download(filename=name)
        except:
            yt.streams.filter(type = "audio").first().download(filename="undefined_music.mp3")
    elif question == 2:
        try:
            yt.streams.filter(progressive=True, file_extension='mp4', res="720p").first().download(filename=namevid)
        except:
            yt.streams.filter(progressive=True, file_extension='mp4', res="720p").first().download(filename="undefined_video.mp4")

try:
    download_audio()
except:
    print("Что-то не то")