import os
from yt_dlp import YoutubeDL
import re

def dlyoutubeasmp3(a_tagUrl, a_title):

    # 初期化
    t_targetUrl = a_tagUrl
    t_title = a_title
    t_outputBaseDir = "D:\\11_github\\sound\\result\\dlyoutubemp3"
    t_cookie_path = "D:\\11_github\\sound\\src\\dlYoutube\\youtube.com_cookies.txt"
    t_output_archive = "D:\\11_github\\sound\\result\\dlyoutubemp3\\archive.txt"


    os.makedirs(t_outputBaseDir, exist_ok=True)
    t_outputFile = t_outputBaseDir + '/'  + t_title + '/' + t_title.replace("/","_").replace("–","") + '.mp3'

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': t_outputFile,
        'cookiefile': t_cookie_path,
        'download_archive': t_output_archive,
    }

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([t_targetUrl])

    return os.path.join(os.getcwd(),t_outputFile)