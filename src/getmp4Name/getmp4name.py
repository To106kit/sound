from youtubesearchpython import VideosSearch,Video
def getmp4name(a_tagUrl):
    # 初期化
    t_tagUrl = a_tagUrl
    videoInfo = Video.getInfo(t_tagUrl)
    # print(videoInfo["title"])
    t_title = videoInfo["title"]
    # print(videoInfo["description"])
    return t_title.replace(' ', '').replace('\u3000', '').replace('/','')