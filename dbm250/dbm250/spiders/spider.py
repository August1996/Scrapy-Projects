# -*- coding:utf-8 -*-
import scrapy

class Dbm250Spider(scrapy.Spider):
	name ='dbm250'
	start_urls = [
	'http://movie.douban.com/top250'
	]

	def parse(self,response):
		pages = response.css('.paginator a::attr(href)')
		for page in pages:
			full_url = response.urljoin(page.extract())
			yield scrapy.Request(full_url,callback = self.parse_page)

	def parse_page(self,response):
		hrefs = response.css('.hd a::attr(href)')
		for href in hrefs:
			yield scrapy.Request(href.extract(),callback = self.parse_url)

	def parse_url(self,response):
		return {
		'name' : response.xpath('//span[@property="v:itemreviewed"]//text()').extract(),
		'score' : response.xpath('//span[@property="v:average"]//text()').extract(),
		'year' : response.xpath('//span[@class="year"]//text()').extract(),
		'actors' : response.xpath('//a[@rel="v:starring"]//text()').extract(), 
		'type' : response.xpath('//a[@property="v:genre"]//text()').extract(),
		'link' : response.url,
		}
