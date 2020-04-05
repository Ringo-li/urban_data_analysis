# -*- coding: utf-8 -*-

import scrapy

from article.items import ArticleItem

class WanFang(scrapy.Spider):
    name = "upf"
    start_urls = []
    for year in range(2015,2020):
        for month in range(1,13):
            for date in range(1,24):
                url = 'http://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFQ\
&dbname=CJFDLAST2016&filename=CSGH{}{}{}'.format(year,str(month).zfill(2),str(date).zfill(3))
                start_urls.append(url)

##############################第二次关键词爬取########################
    def parse(self, response):
        item = ArticleItem()
        item['title'] = response.xpath('//*[@class="wxTitle"]/h2/text()').extract()[0].strip()
        item['date'] = response.xpath('//div[@class="sourinfo"]/p[3]/a/text()').extract()[0].strip().replace(';\r\n','')

        if response.xpath('//div[@class="wxBaseinfo"]/p[2]/label[@id="catalog_FUND"]'):
            keywords = response.xpath('//div[@class="wxBaseinfo"]/p[3]/a/text()').extract()
            item['keywords'] = [i.strip().replace(';','')  for i in keywords]
            fund = response.xpath('//div[@class="wxBaseinfo"]/p[2]/a/text()').extract()
            item['fund'] = [i.strip().replace('；','') for i in fund]
        else:
            keywords = response.xpath('//div[@class="wxBaseinfo"]/p[2]/a/text()').extract()
            item['keywords'] = [i.strip().replace(';','') for i in keywords]
            item['fund'] = []
        print(response)
        return item


##############第一次其他信息爬取####################
    # def parse(self, response):
    #     print('a new page'.center(60,'='))
    #     item = ArticleItem()
    #     item['title'] = response.xpath('//*[@class="wxTitle"]/h2/text()').extract()[0].strip()
    #     item['abstract'] = response.xpath('//*[@class="wxBaseinfo"]//*[@id="ChDivSummary"]/text()').extract()[0]
    #     authors_info =  response.xpath('//div[@class="author"]/span/a/@onclick').extract()
    #     authors_list = [i.strip()[21:-3].replace('\'','').split(',') for i in authors_info]
    #     item['date'] = response.xpath('//div[@class="sourinfo"]/p[3]/a/text()').extract()[0].strip().replace(';\r\n','')
    #     if response.xpath('//div[@class="wxBaseinfo"]/p[2]/label[@id="catalog_FUND"]'):
    #         keywords = response.xpath('//div[@class="wxBaseinfo"]/p[3]/a/text()').extract()
    #         item['keywords'] = [i.strip().replace(';','')  for i in keywords]
    #         fund = response.xpath('//div[@class="wxBaseinfo"]/p[2]/a/text()').extract()
    #         item['fund'] = [i.strip().replace('；','') for i in fund]
    #     else:
    #         keywords = response.xpath('//div[@class="wxBaseinfo"]/p[2]/a/text()').extract()
    #         item['keywords'] = [i.strip().replace(';','') for i in keywords]
    #         item['fund'] = []
    #     for author in authors_list:
    #         author_url = 'http://kns.cnki.net/kcms/detail/knetsearch.aspx?sfield=au&skey={}&code={}'.format(author[0],author[1])
    #         # item['ins'] = author_url
    #         yield scrapy.Request(author_url, meta={'item': item},callback=self.parse_author) 

    # def parse_author(self,response):
    #     item = response.meta['item']
    #     item['author'] = response.xpath('//div[@class="info"]/h2[@class="name"]/text()').extract()[0]
    #     item['ins'] = response.xpath('//div[@class="info"]/p[@class="orgn"]/a/text()').extract()[0]
    #     item['author_num'] = response.xpath('//div[@class="info"]/p[@class="num"]/span[1]/text()').extract()[0].strip()
    #     return item