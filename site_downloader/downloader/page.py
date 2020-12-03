import os

from site_downloader.downloader.html_structure import fix_links
from site_downloader.downloader.site_structure import create_structure
from site_downloader.downloader.statics import download_statics
from site_downloader.downloader.utils import get_file_location


def download_page(response):
    create_structure(response)
    download_statics(response)

    file_path = os.path.dirname(os.path.abspath(__file__)) + '/../../' + get_file_location(response)
    with open(file_path, 'w+') as f:
        html = fix_links(response)
        f.write(html)
