import os
from urllib.request import urlretrieve
from bs4 import BeautifulSoup


def download_statics(response):
    splited_url = response.url.split('/')
    bs = BeautifulSoup(response.text, 'html.parser')
    path = os.path.dirname(os.path.abspath(__file__)) + '/../../' + splited_url[2] + '/static_files/img/' + ''.join(f + '/' for f in splited_url[3:-1])

    for img in bs.find_all('img'):
        if 'src' in img.attrs:
            img_src = img.attrs['src']
            img_path = path + img.attrs['src'].split('/')[-1]
            urlretrieve(img_src, img_path)
