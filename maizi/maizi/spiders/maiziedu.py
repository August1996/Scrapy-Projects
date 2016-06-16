# -*- coding: utf-8 -*-
import scrapy
import sys
from scrapy.http import Request, FormRequest
reload(sys)
sys.setdefaultencoding("utf-8")
class MaizieduSpider(scrapy.Spider):
    name = "maiziedu"
    start_urls = [
    'http://www.maiziedu.com'
    ]
    

    def start_requests(self):
        return [Request(url = 'http://www.maiziedu.com/',callback = self.login)]

    def login(self,response):
        logindata = {
            'account_l':'xxx',
            'password_l':'xxx'
        }
        #这是用户信息

        header = {
            'HOST': 'www.maiziedu.com',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://www.maiziedu.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:42.0) Gecko/20100101 Firefox/42.0'
        }
        return FormRequest.from_response(
            response = response,
            url = 'http://www.maiziedu.com/user/login',
            formdata = logindata,
            method = 'post',
            headers = header,
            callback = self.parse_page
            )

    def parse_page(self,response):
        return Request('http://www.maiziedu.com/group/common/course/',callback = self.parse_url)

    def parse_url(self,response):
        links = response.css('.col-in a::attr(href)').extract()
        for link in links:
            full_url = response.urljoin(link)
            yield Request(full_url,callback = self.parse_detail)

    def parse_detail(self,response):
        yield{
            'name' : response.css('.course-lead dt::text').extract(),
            'views' : response.css('.pull-right p::text').extract(),
            'score' : response.css('.raty-num::text').extract(),
            'teacher' : response.css('.teacher .media-body .media-heading a::text').extract(),
            'link' : response.url
        }