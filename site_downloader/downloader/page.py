import os

from site_downloader.downloader.site_structure import create_structure


def download_page(response):
    create_structure(response)
    file_name = response.url.split('/')[-1] + '.html'
    file_name = 'index.html' if file_name == '.html' else file_name

    file_path = os.path.dirname(os.path.abspath(__file__)) + '/../../pythonscraping.com/' + file_name
    with open(file_path, 'w+') as f:
        f.write(response.text)
