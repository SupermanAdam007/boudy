# -*- coding: utf-8 -*-
import scrapy
from boudy_crawler.items import Bouda


class Languages:
    CZ = 'cz'
    EN = 'en'


class BoudySpider(scrapy.Spider):
    name = 'boudy'
    allowed_domains = ['boudy.info']
    start_urls = [
        f'http://boudy.info/bouda.php?txt={Languages.CZ}&id={bouda_id}' 
        for bouda_id in range(1, 3)]
    MIN_ID = 1
    MAX_ID = 1760

    def parse(self, response):
        self.log(f'URL: {response.url}')
        bouda = Bouda()
        bouda['nadpis'] = response.xpath('/html/body/div/div/div[3]').get()
        yield bouda
