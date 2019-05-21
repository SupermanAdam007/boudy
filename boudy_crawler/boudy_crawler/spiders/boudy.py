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
    BASE_URL = 'http://boudy.info/'
    start_urls = [
        f'http://boudy.info/bouda.php?txt={Languages.CZ}&id={bouda_id}' 
        for bouda_id in range(1, 2)]
    MIN_ID = 1
    MAX_ID = 1760

    def parse(self, response):
        bouda = Bouda()
        bouda['source_url'] = response.url
        bouda['nadpis'] = response.xpath('/html/body/div/div/div[3]/text()').get().strip()

        okolis = response.xpath('//div[@class="sloupek_okoli_link"]')
        okoli_list = []
        for okoli in okolis:
            okoli_list.append(
                {
                    'id': okoli.attrib.get('id'),
                    'img': f"{BoudySpider.BASE_URL}{okoli.xpath('img').attrib.get('src')}",
                    'link': f"{BoudySpider.BASE_URL}{okoli.xpath('a').attrib.get('href')}",
                }
            )
        bouda['okoli'] = okoli_list

        main_img_all = response.xpath('/html/body/div/div/div[6]/div[9]/div[1]/a/img')
        main_img = f"{BoudySpider.BASE_URL}{main_img_all.attrib.get('src')}"
        bouda['main_img'] = main_img

        info_ik_trida_druhs = response.xpath('/html/body/div/div/div[6]/div[9]/div[2]/img')
        info_ik_trida_druh_list = []
        for info_ik_trida_druh in info_ik_trida_druhs:
            info_ik_trida_druh_list.append(
                {
                    'class': info_ik_trida_druh.attrib.get('class'),
                    'img': f"{BoudySpider.BASE_URL}{info_ik_trida_druh.attrib.get('src')}",
                    'title': info_ik_trida_druh.attrib.get('title'),
                }
            )
        bouda['info_ik_trida_druh'] = info_ik_trida_druh_list

        bouda['info_pocet'] = int(response.xpath('//div[@class="info_pocet"]/text()').get() or '0')
        bouda['info_pocet_max'] = int(response.xpath('//div[@class="info_pocet_max"]/text()').get() or '0')

        info_iks = response.xpath('//img[@class="info_ik"]')
        info_ik_list = []
        for info_ik in info_iks:
            info_ik_list.append(
                {
                    'src': f"{BoudySpider.BASE_URL}{info_ik.attrib.get('src')}",
                    'title': info_ik.attrib.get('title'),
                }
            )
        bouda['info_ik'] = info_ik_list

        bouda['info_txt'] = ''.join(response.xpath('//div[@class="info_txt"]/text()').getall()).strip()
        bouda['info_gps_1'] = response.xpath('//span[@class="info_gps_1"]/text()').get().strip().replace('\n', ' ')


        yield bouda

    # TODO: parse all comments from for ex. http://boudy.info/bouda.php?txt=cz&id=1&par=poz
    def parse_comments(self, response):
        item = response.meta['item']
        # item['comments'] = response.url
        return item

    # TODO: read all comments from for ex. http://boudy.info/bouda.php?txt=cz&id=1&par=obr
    def parse_imgs(self, response):
        item = response.meta['item']
        # item['imgs'] = response.url
        return item
