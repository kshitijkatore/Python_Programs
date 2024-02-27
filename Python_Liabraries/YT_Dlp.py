# Download youtube videos using python
# pip install yt-dlp

import yt_dlp

# Enter the url for the download
url = input("Enter video url:")
ydl_opts = {}

with yt_dlp.YoutubeDl(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded sucessfully")