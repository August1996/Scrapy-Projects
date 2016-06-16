# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys

class ObderrorPipeline(object):

	def __init__(self):
		reload(sys)
		sys.setdefaultencoding('utf-8')

	def process_item(self, item, spider):
		sql = ("insert obdcode values(null,'%s','%s','%s','%s','%s','%s','%s');" % (item['usefor'], item['suit'],item['code'], item['cndesc'], item['endesc'], item['belong'], item['reason']))
		f = open('sql.txt','a+')
		f.write(sql+'\n')
		f.close()
		return item
