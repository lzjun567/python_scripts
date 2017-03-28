# encoding: utf-8
__author__ = 'liuzhijun'

import scrapy
from scrapy.crawler import CrawlerProcess

class ZhihuSpider(scrapy.Spider):
    name = "zhihu"

    def start_requests(self):
        url = 'https://www.zhihu.com/question/40007169/answer/146281325'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file_name = "zhihu.html"
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % file_name)

if __name__ == '__main__':
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3047.4 Safari/537.36'
    })
    process.crawl(ZhihuSpider)
    process.start()