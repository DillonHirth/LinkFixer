import os
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

EMAIL = os.getenv('IFUNNY_EMAIL')
PASS = os.getenv('IFUNNY_PW')
headers = {
    'user-agent': 'linkFixer/0.0.1',
    'Accept-Language': 'en-US,en;q=0.5',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}


def get_url_src(url):
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
    else:
        print("bad response:", response.status_code)

# get_url_src('https://ifunny.co')
