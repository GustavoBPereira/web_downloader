import sys
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from site_downloader.spiders.sites import SiteSpider

if __name__ == '__main__':
    try:
        os.remove('sites.json')
    except FileNotFoundError:
        pass

    process = CrawlerProcess(get_project_settings(), {
        'FEEDS': {
            'sites.json': {'format': 'json'},
        },
    })

    process.crawl(SiteSpider)
    process.start()

    if len(sys.argv) > 1 and sys.argv[1] in ['--test', 'test']:
        import json

        with open('sites.json') as json_file:
            crawled_data = json.load(json_file)
            expect = [
                {'url': 'http://pythonscraping.com/', 'title': 'Collecting More Data from the Modern Web'},
                {'url': 'http://pythonscraping.com/node/5', 'title': 'About the Author'},
                {'url': 'http://pythonscraping.com/blog', 'title': 'Posts to Scrape'},
                {'url': 'http://pythonscraping.com/node/15', 'title': 'About the Book'}
            ]
            for elem in expect:
                try:
                    assert elem in crawled_data
                except AssertionError:
                    raise AssertionError('sites.json file with unexpected data...')
            print('Everything ok...')
