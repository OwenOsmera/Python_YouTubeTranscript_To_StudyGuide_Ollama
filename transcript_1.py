"""
transcript_1.py
3/26/26

"""

from youtube_transcript_api import YouTubeTranscriptApi
from pytubefix import YouTube

# defualt file name
DEFUALT = "Example.txt"
DEFUALT_ID = "111111111"
DEFUALT_URL = "JFLKSJNLKJNF.com"

# create a usable function
def gen_readable_file(id=DEFUALT_ID, url=DEFUALT_URL):
    # get tile for file name
    yt = YouTube(url)
    video_title = yt.title

    # Set object and fetch english captions
    yta = YouTubeTranscriptApi()
    fetch = yta.fetch(id, languages=["en"])

    # create plain text dictionaries
    tx = fetch.to_raw_data()

    with open(video_title+".txt", "w", encoding="utf-8") as f:
        for item in tx:
            f.write(item["text"] + "\n")

    return video_title

def main():
    # create file with id
    gen_readable_file("87t6P5ZHTP0", "https://www.youtube.com/watch?v=87t6P5ZHTP0&list=PLG49S3nxzAnnOmvg5UGVenB_qQgsh01uC")

if __name__ == "__main__":
    main()




