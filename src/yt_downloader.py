from youtube_dl import YoutubeDL
from pytube import YouTube
import json
import os

playlist = str(input("¿Qué playlist deseas descargar? "))

ydl_opts = {
    'ignoreerrors': True
}

ydl = YoutubeDL(ydl_opts)

output = ydl.extract_info(playlist,download=False)

for a in output.get("entries"):
    yt = YouTube(a.get("webpage_url"))
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="./downloads")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'

    os.rename(out_file, new_file)

print("Descarga completada")