from pytube import YouTube

link=str(input("plz enter the link"))
youtube_1 = YouTube(link)
print(youtube_1.title)
print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all()

# only for audio-----------------------
# videos = youtube_1.streams.filter(only_audio=True)


vid = list(enumerate(videos)) # for itrate all pixcle availabe
for i in vid:
    print(i)

strm =int(input("enter"))
videos[strm].download(r"C:\Users\Dell\Downloads\vedio")
print("successfully download")


#------------------------playList download------------------
# from pytube import Playlist
#
# py = Playlist("playlist url")
# print(py.title)
# print(py.description)
#
# for video in py.videos:
#     video.streams.first().download()
