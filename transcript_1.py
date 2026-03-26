"""
transcript_1.py
3/26/26

"""

from youtube_transcript_api import YouTubeTranscriptApi

# defualt file name
DEFUALT = "Example.txt"
DEFUALT_ID = "111111111"

# create a usable function
def gen_readable_file(filename=DEFUALT, id=DEFUALT_ID):
    # Set object and fetch english captions
    yta = YouTubeTranscriptApi()
    fetch = yta.fetch(id, languages=["en"])

    # create plain text dictionaries
    tx = fetch.to_raw_data()

    with open(filename, "w", encoding="utf-8") as f:
        for item in tx:
            f.write(item["text"] + "\n")

def main():
    # create file with id
    gen_readable_file("cool.txt", "87t6P5ZHTP0")

if __name__ == "__main__":
    main()




