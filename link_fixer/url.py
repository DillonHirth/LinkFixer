"""
bs4: beautiful soup, used for html parsing
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

headers = {
    'user-agent': 'linkFixer/0.0.1',
    'Accept-Language': 'en-US,en;q=0.5',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}


def get_url_src(url):
    """os module for .env file"""
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        only_meta_tags = SoupStrainer("meta")
        print("request status_code:", response.status_code)
        soup = BeautifulSoup(response.content, 'html.parser', parse_only=only_meta_tags)

        for link in soup.find_all('meta'):
            if link.get('property') == "og:video:secure_url":
                direct_link = (link.get('content'))
                break
        return direct_link
    return "bad response:" + str(response.status_code)
