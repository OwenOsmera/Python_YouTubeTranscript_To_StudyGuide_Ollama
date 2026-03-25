from youtube_transcript_api import YouTubeTranscriptApi

ytt = YouTubeTranscriptApi()
fetched = ytt.fetch("zODZ0i-Iark", languages=["en"])

# If you want plain list-of-dicts:
tx = fetched.to_raw_data()

with open("op.txt", "w", encoding="utf-8") as f:
    for item in tx:
        f.write(item["text"] + "\n")