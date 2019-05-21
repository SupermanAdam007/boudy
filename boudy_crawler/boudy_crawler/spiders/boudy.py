# -*- coding: utf-8 -*-
import scrapy


class Languages:
    CZ = 'cz'
    EN = 'en'

class BoudySpider(scrapy.Spider):
    name = 'boudy'
    allowed_domains = ['boudy.info']
    start_urls = ['http://boudy.info/']
    URL_TEMPLATE = 'http://boudy.info/bouda.php?txt={}&id={}'
    MIN_ID = 1
    MAX_ID = 1760

    def parse(self, response):
        pass
