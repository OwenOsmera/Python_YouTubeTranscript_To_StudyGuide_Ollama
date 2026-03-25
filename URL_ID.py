"""
3/25/26
URL_ID.py

"""

import re

def extract_video_id(url):
    """
    Extracts the 11-character video ID from a YouTube URL.
    Works with standard watch, embed, and youtu.be links.
    """
    match = re.search(r'(?:v=|/)([0-9A-Za-z_-]{11})', url)
    if not match:
        raise ValueError(f"Invalid YouTube URL: {url}")
    return match.group(1)

def main():
    # Example usage:
    url = input("URL: ")
    video_id = extract_video_id(url)
    print(video_id)  # Output: dQw4w9WgXcQ

if __name__ == "__main__":
    main()