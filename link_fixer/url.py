"""
bs4: beautiful soup, used for html parsing
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


def get_url_src(url):
    """os module for .env file"""
    video_direct_link = None
    image_direct_link = None
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Firefox/110.0",
        "Accept": "image/avif,image/webp,*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        # "Upgrade-Insecure-Requests": "1",
        # "Cache-Control": "max-age=0",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        only_meta_tags = SoupStrainer("meta")
        print("request status_code:", response.status_code)

        soup = BeautifulSoup(response.content, "html.parser", parse_only=only_meta_tags)

        for link in soup.find_all("meta"):
            if link.get("property") == "og:video:secure_url":
                video_direct_link = link.get("content")
                print("direct_link:", video_direct_link)
            elif link.get("property") == "og:image:secure_url":
                image_direct_link = link.get("content")
                print("direct_link:", image_direct_link)
        if video_direct_link:
            return video_direct_link
        return image_direct_link
    return "bad response:" + str(response.status_code)
