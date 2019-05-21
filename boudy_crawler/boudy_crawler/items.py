# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Bouda(scrapy.Item):
    source_url = scrapy.Field()
    nadpis = scrapy.Field()
    okoli = scrapy.Field()
    main_img = scrapy.Field()
    info_ik_trida_druh = scrapy.Field()
    info_pocet = scrapy.Field()
    info_pocet_max = scrapy.Field()
    info_ik = scrapy.Field()
    info_txt = scrapy.Field()
