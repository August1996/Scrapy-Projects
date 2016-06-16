# -*- coding: utf-8 -*-
import scrapy

brands_id = 0	
types_id = 0	
cars_id = 0	

class CarinfosSpider(scrapy.Spider):
	name='carinfos'
	start_urls = (
        'http://www.xgo.com.cn/brand.html',
    )

	
	def parse(self, response):
		links = response.xpath('//div[@class="l"]/a[1]/@href').extract()
		for link in links:
			yield scrapy.Request(link,callback = self.parse_brand,meta={'brands_id':brands_id,'types_id':types_id,'cars_id':cars_id})

	def parse_brand(self,response):
		# brands_id = response.meta['brands_id']
		# types_id = response.meta['types_id']
		# cars_id = response.meta['cars_id']

		global brands_id
		global types_id
		global cars_id

		brand_id = brands_id
		brands_id = brands_id + 1
		brand_name = response.css('.brand_logo+h1::text').extract()
		brand_img = response.css('.brand_logo img::attr(src)').extract()
    	#记录brand_id,brand_name,brand_img

		links = response.css('.car-list p a::attr(href)').extract()
		for i in range(len(links)):
			full_url = response.urljoin(links[i]) + 'items.html'
			yield scrapy.Request(full_url,callback = self.parse_type,meta={'brand_id':brand_id,'brand_name':brand_name,'brands_id':brands_id,'types_id':types_id,'cars_id':cars_id})

	def parse_type(self,response):
		# brands_id = response.meta['brands_id']
		# types_id = response.meta['types_id']
		# cars_id = response.meta['cars_id']
		global brands_id
		global types_id
		global cars_id

		brand_id = response.meta['brand_id']
		brand_name = response.meta['brand_name']
		type_id = types_id
		types_id = types_id + 1
		type_name = response.css('.car_banner_l .num::text').extract()
		#记录brand_id,brand_name,type_id,type_name
		links = response.css('.car_name ul li p a::attr(href)').extract()
		for link in links:
			yield scrapy.Request(link,callback = self.parse_cars,meta={'brand_id':brand_id,'brand_name':brand_name,'type_id':type_id,'type_name':type_name,'brands_id':brands_id,'types_id':types_id,'cars_id':cars_id})

	def parse_cars(self,response):
		# brands_id = response.meta['brands_id']
		# types_id = response.meta['types_id']
		# cars_id = response.meta['cars_id']
		global brands_id
		global types_id
		global cars_id
		brand_id = response.meta['brand_id']
		brand_name = response.meta['brand_name']
		type_id = response.meta['type_id']
		type_name = response.meta['type_name']
		link = response.urljoin(response.xpath('//div[@class="cxk-navbox"]/ul/li[4]/a/@href').extract()[0])
		yield scrapy.Request(link,callback = self.parse_car,meta={'brand_id':brand_id,'brand_name':brand_name,'type_id':type_id,'type_name':type_name,'brands_id':brands_id,'types_id':types_id,'cars_id':cars_id})

	def parse_car(self,response):
		manufacturers1_id = response.meta['brand_id']
		manufacturers1 = response.meta['brand_name']
		manufacturers2_id = response.meta['type_id']
		manufacturers2 = response.meta['type_name']
		global brands_id
		global types_id
		global cars_id

		# cars_id = response.meta['cars_id']

		car_id = cars_id
		cars_id = cars_id + 1
		#记录brand_id,type_id,car_id,car_info
		name = response.css('.offer_topnav h3 a::text').extract()[0]
		where = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[0]
		level = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[1]
		year = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[2]
		displacement = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[3]
		maximumSpeed = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[4]
		officialAcceleration = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[5]
		ministryOfIntegratedFuelConsumption = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[6]
		vehicleQuality = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[8]
		longHighWith = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[9]
		bodyStructure1 = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[15]
		doorNum = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[16]
		seatNum = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[17]
		mailVolume = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[18]
		model = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[20]
		intakeForm = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[22]
		fuelForm = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[36]
		fuel = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[37]
		fuleWay = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[38]
		environmentalProtection = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[41]
		powerType = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[42]
		gearbox = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[47]
		drivingMethod = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[50]
		frontSuspension = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[53]
		backSuspension = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[54]
		bodyStructure2 = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[56]
		frontBrakeType = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[57]
		brakeType = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[58]
		parkingBrakeType = response.xpath('//div[@id="peizhi"]//td[@class="bor-l"]/text()').extract()[59]
		price = response.css('.cxkmoneys .cxk-jg::text').extract()

		yield {
				'manufacturers1_id':manufacturers1_id,
				'manufacturers1':manufacturers1,
				'manufacturers2_id':manufacturers2_id,
				'manufacturers2':manufacturers2,
				'id' : car_id,
				'name' :name,
				'where' :where,
				'level' :level,
				'year' :year,
				'displacement' :displacement,
				'maximumSpeed' :maximumSpeed,
				'officialAcceleration' : officialAcceleration,
				'ministryOfIntegratedFuelConsumption' : ministryOfIntegratedFuelConsumption,
				'vehicleQuality' : vehicleQuality,
				'longHighWith' : longHighWith,
				'bodyStructure1' :bodyStructure1,
				'doorNum' :doorNum,
				'seatNum' :seatNum,
				'mailVolume' :mailVolume,
				'model' :model,
				'intakeForm' :intakeForm,
				'fuelForm' :fuelForm,
				'fuel' :fuel,
				'fuleWay' :fuleWay,
				'environmentalProtection' :environmentalProtection,
				'powerType' :powerType,
				'gearbox' :gearbox,
				'drivingMethod' :drivingMethod,
				'bodyStructure2' :bodyStructure2,
				'frontBrakeType' :frontBrakeType,
				'brakeType' :brakeType,
				'parkingBrakeType' :parkingBrakeType,
				'price' :price,
		}