# -*- coding:utf-8 -*-
import scrapy
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class TBMMSpider(scrapy.Spider):
	name = 'tbmm'
	start_urls=[]
	for x in range(1,11):
		start_urls.append("https://mm.taobao.com/json/request_top_list.htm?page="+str(x))
	def parse(self,response):
		names = response.css(".lady-name::text").extract()
		ages = response.css(".top em strong::text").extract()
		froms = response.css(".top span::text").extract()
		tmp_avator = response.css(".lady-avatar img::attr(src)").extract()
		tmp_links = response.css(".lady-name::attr(href)").extract()
		avatars = []
		for avatar in tmp_avator:
			avatars.append("https:"+avatar)
		links = []
		for link in tmp_links:
			links.append("https:"+link)
		for x in range(1,11):
			if(not os.path.exists(names[x])):
				os.mkdir(names[x])
			text ='<meta charset="utf-8"><table><tr><th>姓名</th><th>来自</th><th>年龄</th><th>头像</th></tr>'
			text = text + '<tr><td><a href="'+links[x]+'">'+names[x]+'</a></td><td>'+froms[x]+'</td><td>'+ages[x]+'</td><td><img src="'+avatars[x]+'"></td></tr>'
			text = text + '</table>'
			open(os.path.join(names[x],'intro.html'),'wb').write(text)
