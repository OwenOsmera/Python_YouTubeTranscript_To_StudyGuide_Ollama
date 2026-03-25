from youtube_transcript_api import YouTubeTranscriptApi

# If the video id starts with a hyphen you will have to mask the hyphen
#Video also needs to have subtitles

# youtube_transcript_api "\-abc123"

# ---Main Code --

outls = []

tx = YouTubeTranscriptApi().get_transcript("zODZ0i-Iark", languages=["en"]) 

for i in tx:
    outtxt = (i['text'])
    outls.append(outtxt)

    with open("op.txt", "a") as opf:
        opf.write(outtxt + "\n")


