from youtube_dl import YoutubeDL
import moviepy.editor as mp
from pytube import YouTube
import json
import os

playlist = str(input("¿Qué playlist deseas descargar? "))

ydl_opts = {
    'ignoreerrors': True
}

ydl = YoutubeDL(ydl_opts)

output = ydl.extract_info(playlist,download=False)

for i,a in enumerate(output.get("entries")):
    print(i,a.get("webpage_url"))

    yt = YouTube(a.get("webpage_url"))
    video = yt.streams.filter(res="360p").first() # video = yt.streams.filter().get_highest_resolution()
    out_file = video.download(output_path="./downloads")

    clip = mp.VideoFileClip(out_file)
    
    clip.audio.write_audiofile(os.path.join("./downloads",out_file.split("./downloads\\",1)[1][0:-4]+str(i)+".mp3"), bitrate="128k")
    
    clip.close()

    os.remove(os.path.join("./downloads/",out_file.split("./downloads\\",1)[1][0:-4]+".mp4"))

print("----------------------")
print("Canciones descargadas")
print("----------------------")