import os
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from site_downloader.downloader.html_structure import fix_links
from site_downloader.downloader.site_structure import create_structure
from site_downloader.downloader.statics import download_statics
from site_downloader.downloader.utils import get_file_location, is_internal_link
from site_downloader.downloader.data import Link, Img, Js, Css


def download_page(response):
    create_structure(response)
    download_statics(response)

    file_path = os.path.dirname(os.path.abspath(__file__)) + '/../../' + get_file_location(response)
    with open(file_path, 'w+') as f:
        html = fix_links(response)
        f.write(html)


class Response(object):

    def __init__(self, scrapy_response, project_dir):
        self.scrapy_response = scrapy_response
        self.bs = BeautifulSoup(scrapy_response.text, 'html.parser')
        self.links = []
        self.img = []
        self.js = []
        self.css = []
        self.project_dir = project_dir

        for link in self.bs.find_all('a'):
            if 'href' in link.attrs and is_internal_link(self.scrapy_response, link.attrs['href']):
                self.links.append(Link(link.attrs['href']))

        # for img in self.bs.find_all('img'):
        #     if 'src' in img.attrs:
        #         self.img.append(Img(img.attrs['src']))
        #
        # for js in self.bs.find_all('script'):
        #     if 'src' in js.attrs:
        #         self.js.append(Js(js.attrs['src']))
        #
        # for css in self.bs.find_all('link'):
        #     if 'type' in css.attrs and css.attrs['type'] == 'text/css' and 'href' in css.attrs:
        #         self.css.append(Css(css.attrs['href']))

    @property
    def url(self):
        return urlparse(self.scrapy_response.url)

    @property
    def file_name(self):
        file_name = 'index' if self.url.path == '' else self.url.path
        file_name += '.html' if not file_name.endswith('.html') else ''
        return file_name

    @property
    def file_path(self):
        return self.project_dir + self.file_name

    def save(self):
        # salva o html baseado na estrutura do bs
        # create_structure(response)
        # file_path = get_file_location(response)
        # download_statics(response)

        with open(self.file_path, 'w+') as f:
            f.write(self.scrapy_response.text)
        self.save_data()

    def save_data(self):
        for link in self.links:
            self.bs.replace(link.origin_url, link.relative_path)
            link.save()
        # for img in self.img:
        #     self.bs.replace(img.origin_url, img.relative_path)
        #     img.save()
        # for js in self.js:
        #     self.bs.replace(js.origin_url, js.relative_path)
        #     js.save()
        # for css in self.css:
        #     self.bs.replace(css.origin_url, css.relative_path)
        #     css.save()
        self.save()
