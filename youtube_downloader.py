from pytube import YouTube


def download_youtube_video(url):
    yt = YouTube(url)
    videos = yt.streams.all()

    for index, value in enumerate(videos):
        print(str(index), ".", str(value))

    n = int(input("Enter your choice: "))
    vid = videos[n-1]

    print("Downloading the video ...")

    vid.download()

    print("Downloaded the video successfully")


if __name__ == '__main__':
    download_youtube_video("https://www.youtube.com/watch?v=n2u81Ujc93g")
