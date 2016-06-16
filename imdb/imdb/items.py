# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    name = scrapy.Field()
    publish_date = scrapy.Field()
    last_time = scrapy.Field()
    classifications = scrapy.Field()
    score = scrapy.Field()
    link = scrapy.Field()
