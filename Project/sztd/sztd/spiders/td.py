# -*- coding: utf-8 -*-
import scrapy
from sztd.items import SztdItem

class TdSpider(scrapy.Spider):
    name = 'td'
    allowed_domains = ['zrzy.jiangsu.gov.cn']
    start_urls = ['http://zrzy.jiangsu.gov.cn/gtapp/xxgk/tdsc_getGdxmList.action?xzqhdm=320500&starttime=2019-01-01']

    def parse(self, response):
        # url = response.url
        print('=========================================')
        res = response.xpath('//a/@href').extract()
        for url in res[:-4]:
            url = 'http://zrzy.jiangsu.gov.cn/gtapp/xxgk/' + url.replace('\\"','')
            yield scrapy.Request(url,callback=self.parse1)

    def parse1(self,response):
        item = SztdItem()
        item['TD_ZL'] = response.xpath('//span[@id="TD_ZL"]/text()').extract_first()
        item['XZQ_DM']  = response.xpath('//span[@id="XZQ_DML"]/text()').extract_first()
        item['XM_MC']  = response.xpath('//span[@id="XM_MC"]/text()').extract_first()
        item['GY_MJ']  = response.xpath('//span[@id="GY_MJ"]/text()').extract_first()
        return item







