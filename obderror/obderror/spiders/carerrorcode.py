# -*- coding: utf-8 -*-
import scrapy
from obderror.items import ObderrorItem

class CarerrorcodeSpider(scrapy.Spider):
    name = "carerrorcode"
    start_urls = (
        'http://chezg.cn/OBDCode/List/P0/',
        'http://chezg.cn/OBDCode/List/P1/',
        'http://chezg.cn/OBDCode/List/P2/',
        'http://chezg.cn/OBDCode/List/P3/',
        'http://chezg.cn/OBDCode/List/B/',
        'http://chezg.cn/OBDCode/List/U/',
        'http://chezg.cn/OBDCode/List/C/',
    )

    def parse(self, response):
        links = response.css('.content a::attr(href)').extract()
        usefor = response.css('.sy h4::text')[1].extract()
        preLink = ''
        for link in links:
        	if preLink != link:
        		full_url = response.urljoin(link)
        		yield scrapy.Request(full_url,callback = self.parse1,meta={'usefor':usefor})
        	preLink = link

    def parse1(self,response):
    	usefor = response.meta['usefor']
        suits = response.css('.th::text').extract()
        datas = response.css('.table1 tr td')
        i = 0
        for suit in suits:
            if len(datas[i].css('td::text').extract()) != 0:
                code = datas[i].css('td::text').extract()[0]
            else:
                code = ''
            i = i +1

            if len(datas[i].css('td::text').extract()) != 0:
                cndesc = datas[i].css('td::text').extract()[0]
            else:
                cndesc = ''
            i = i +1

            if len(datas[i].css('td::text').extract()) != 0:
                endesc = datas[i].css('td::text').extract()[0]
            else:
                endesc = ''
            i = i +1

            if len(datas[i].css('td::text').extract()) != 0:
                belong = datas[i].css('td::text').extract()[0]
            else:
                belong = ''
            i = i +1

            if len(datas[i].css('td::text').extract()) != 0:
                reason = datas[i].css('td::text').extract()[0]
            else:
                reason = ''
            i = i +1

            item = ObderrorItem()
            item['usefor'] = usefor
            item['suit'] = suit
            item['code'] = code
            item['cndesc'] = cndesc
            item['endesc'] = endesc
            item['belong'] = belong
            item['reason'] = reason
            yield item