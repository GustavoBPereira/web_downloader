from urllib.request import urlretrieve
from bs4 import BeautifulSoup

from site_downloader.downloader.utils import static_path


def download_statics(response):
    bs = BeautifulSoup(response.text, 'html.parser')

    for img in bs.find_all('img'):
        if 'src' in img.attrs:
            img_src = img.attrs['src']
            img_path = static_path(response, 'img') + img.attrs['src'].split('/')[-1]
            urlretrieve(img_src, img_path)
