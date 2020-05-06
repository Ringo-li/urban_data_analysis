# -*- coding: utf-8 -*-
import scrapy
from planning.items import PlanningItem


class PlSpider(scrapy.Spider):
    name = 'pl'
    allowed_domains = ['planning.org.cn']
    start_urls = []
    for i in range(1,11):
        url = 'http://planning.org.cn/news/newslist?cid=12&page={}'.format(str(i))
        start_urls.append(url)

    def parse(self, response):
        item = PlanningItem()
        res = response.xpath('//div[@class="fl w680 overh xh_list_boxb"]/div[@class="zoom mt20 news_list_boxb pb15 f12 l22 pr15"]')
        for i in res:
            item['title'] = i.xpath('h4/a/text()').extract_first()
            item['cont'] = i.xpath('p[1]/text()').extract_first()
            item['time'] = i.xpath('p[2]/text()').extract_first()
            yield item