import scrapy

class ExpdbRemoteSpider(scrapy.Spider):
	name = 'expdbremote'
	start_urls = [
	'https://www.exploit-db.com/remote/'
	]

	def parse(self,response):
		hrefs = response.css('tbody .description a::attr(href)').extract()
		for href in hrefs:
			full_url = response.urljoin(href)
			yield scrapy.Request(full_url,callback = self.parse_exp)
	def parse_exp(self,response):
		return {
		'id' : response.css('.exploit_list tr td::text')[0].extract(),
		'name' : response.xpath('//title/text()').extract(),
		'author' : response.css('.exploit_list tr')[1].css('td strong::text')[1].extract(),
		'time' : response.css('.exploit_list tr')[1].css('td::text')[2].extract(),
		'link' : response.url 
		}

# class StackOverflowSpider(scrapy.Spider):
# 	name = 'stackoverflow'
# 	start_urls = ['https://www.exploit-db.com/remote/']
# 	def parse(self, response):
# 		for href in response.css('tbody .description a::attr(href)'):
# 			full_url = response.urljoin(href.extract())
# 			yield scrapy.Request(full_url, callback=self.parse_question)
# 	def parse_question(self, response):
# 		yield {
# 		'id' : response.css('.exploit_list tr td::text')[0].extract(),
# 		'name' : response.xpath('//title/text()').extract(),
# 		'author' : response.css('.exploit_list tr')[1].css('td strong::text')[1].extract(),
# 		'time' : response.css('.exploit_list tr')[1].css('td::text')[2].extract(),
# 		'link' : response.url ,
# 		}