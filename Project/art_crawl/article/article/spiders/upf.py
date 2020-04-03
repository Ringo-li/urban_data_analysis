# -*- coding: utf-8 -*-

import scrapy

from article.items import ArticleItem

class WanFang(scrapy.Spider):
    name = "upf"
    start_urls = []

    for year in range(2019,2020):
        for month in range(12,13):
            for date in range(1,30):
                url = 'http://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFQ\
&dbname=CJFDLAST2016&filename=CSGH{}{}{}'.format(year,str(month).zfill(2),str(date).zfill(3))
                # print(url)
                start_urls.append(url)

    def parse(self, response):
        item = ArticleItem()
        item['title'] = response.xpath('//*[@class="wxTitle"]/h2/text()').extract()[0].strip()
        item['abstract'] = response.xpath('//*[@class="wxBaseinfo"]//*[@id="ChDivSummary"]/text()').extract()[0]
        item['author'] = response.xpath('//*[@class="wxTitle"]/div[1]/span/a/text()').extract()
        # item['author_num'] =
        # item['ins'] =
        item['date'] = response.xpath('//div[@class="sourinfo"]/p[3]/a/text()').extract()[0].strip().replace(';\r\n','')
        item['keywords'] = response.xpath('//div[@class="wxBaseinfo"]/p[3]/a/text()').extract()
        item['fund'] = response.xpath('//div[@class="wxBaseinfo"]/p[2]/a/text()').extract()
        # print(response)
        return item
