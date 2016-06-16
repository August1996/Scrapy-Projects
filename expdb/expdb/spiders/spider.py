import scrapy
class Expdb(scrapy.Spider):
	name = 'expdb'
	allowed_domains = ['exploit-db.com']
	start_urls = [
	'https://www.exploit-db.com/remote/'
	]

	def parse(self,response):
		urls = []
		hrefs = response.css('.description a::attr(href)')
		for href in hrefs:
			urls.append(href)
			full_url = response.urljoin(href.extract())
			yield scrapy.Request(full_url,callback = self.parse_question)
		with open('urls.txt','wb') as f:
			f.write(urls)
	def parse_question(self,response):
		yield {
		'id' : response.css('.exploit_list tr td::text')[0].extract(),
		'name' : response.xpath('//title/text()').extract(),
		'author' : response.css('.exploit_list tr')[1].css('td strong::text')[1].extract(),
		'time' : response.css('.exploit_list tr')[1].css('td::text')[2].extract(),
		'link' : response.url 
		}