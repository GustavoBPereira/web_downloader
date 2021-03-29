import scrapy


class Site(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()


class Img(scrapy.Item):
    url = scrapy.Field()


class FilesItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()


class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()