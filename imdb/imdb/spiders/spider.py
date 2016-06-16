import scrapy
from imdb.items import ImdbItem

class ImdbSpider(scrapy.Spider):
	name = 'imdb'
	start_urls = [
	'http://www.imdb.com/movies-in-theaters/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2295495382&pf_rd_r=0R6V2AMGAGTFAAB2DC1F&pf_rd_s=right-3&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_otw_hd&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2295495382&pf_rd_r=0R6V2AMGAGTFAAB2DC1F&pf_rd_s=right-3&pf_rd_t=15061&pf_rd_i=homepage'
	]

	def parse(self,response):
		hrefs = response.xpath('//h4[@itemprop="name"]/a/@href')
		for href in hrefs:
			full_url = response.urljoin(href.extract())
			yield scrapy.Request(full_url,callback=self.parse_detail)

	def parse_detail(self,response):
		items = ImdbItem()
		items['name'] = response.css('#prometer_container+.header .itemprop::text').extract()
		items['publish_date'] = response.css('#prometer_container+.header .nobr a::text').extract()
		items['last_time'] = response.css('.infobar time::text').extract()
		items['classifications'] = response.css('.infobar>a>span::text').extract()
		items['score'] = response.css('.star-box .titlePageSprite::text').extract()
		items['link'] = response.url
		yield items