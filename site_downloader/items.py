import scrapy


class Site(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
