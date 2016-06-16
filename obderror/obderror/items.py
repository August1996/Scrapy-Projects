# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ObderrorItem(scrapy.Item):
	usefor = scrapy.Field()
	suit = scrapy.Field()
	code = scrapy.Field()
	cndesc = scrapy.Field()
	endesc = scrapy.Field()
	belong = scrapy.Field()
	reason = scrapy.Field()

