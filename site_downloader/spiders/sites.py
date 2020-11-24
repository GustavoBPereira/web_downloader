from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from site_downloader.downloader.page import download_page
from site_downloader.items import Site


class SiteSpider(CrawlSpider):
    name = 'sites'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/']
    rules = [
        Rule(LinkExtractor(allow='.*'), callback='parse_items', follow=True)
    ]

    def parse_items(self, response):
        site = Site()
        site['url'] = response.url
        site['title'] = str(response.css('h1#page-title::text').extract_first()).strip()
        download_page(response)
        return site
