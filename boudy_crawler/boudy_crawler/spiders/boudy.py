# -*- coding: utf-8 -*-
import scrapy
import json

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
        bouda = Bouda()
        bouda['nadpis'] = response.xpath('/html/body/div/div/div[3]/text()').get()
        okolis = response.xpath('//div[@class="sloupek_okoli_link"]')

        for okoli in okolis:
            okoli_id = okoli.xpath('//div/@id').get()
            self.log(f'okoli_id: {okoli_id}')

        yield bouda

