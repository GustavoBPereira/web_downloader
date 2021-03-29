from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from site_downloader.downloader.page import download_page, Response
from site_downloader.items import Site, FilesItem, ImageItem


class OfflineSpider(CrawlSpider):
    name = 'offline'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/']
    rules = [
        Rule(LinkExtractor(allow='.*'), callback='parse_items', follow=True),
        Rule(LinkExtractor(tags=("link",),allow='.*', deny_extensions=set()), callback='parse_items', follow=True),
        Rule(LinkExtractor(tags=("script",),attrs=("src",),allow='.*', deny_extensions=set()), callback='parse_items', follow=True),
        Rule(LinkExtractor(tags=("img",), attrs=("src",), allow='.*', deny_extensions=set()), callback='parse_imagem_items',follow=True),
    ]
    #  LinkExtractor(tags = ('img','a','area', 'link', 'script'),attrs=('src','href'), deny_extensions=set())

    def parse_items(self, response):
        item = FilesItem()
        item['file_urls'] = [response.url]
        print(response.url)
        yield item

    def parse_imagem_items(self, response):
        item = ImageItem()
        item['image_urls'] = [response.url]
        print(response.url)
        yield item