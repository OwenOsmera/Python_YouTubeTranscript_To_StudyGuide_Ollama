"""
3/25/26
PullURL.py

"""

# pip install pytube
from pytubefix import Playlist

# Defualt paramiters
DEFAULT_URL = "https://www.youtube.com/playlist?list=PLG49S3nxzAnnOmvg5UGVenB_qQgsh01uC"


def gen_link_list(url = DEFAULT_URL):
    # initialize the playlist object
    relist = Playlist(url)

    # get all video urls
    allVids = relist.video_urls

    # create return list
    result_list = []

    for one in allVids:
        result_list.append(one)

    return result_list
        

def main():
    # hold list
    hold = []

    # use function with default
    hold = gen_link_list()

    # print list
    print(hold)

    
if __name__ == "__main__":
    main()

