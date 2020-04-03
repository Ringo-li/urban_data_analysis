import scrapy

from article.items import ArticleItem

class WanFang(scrapy.Spider):
    name = "upf"
    start_url = []

    for year in range(2015,2020):
        for month in range(1,13):
            for date in range(1,30):
                url = 'http://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFQ\
&dbname=CJFDLAST2016&filename=CSGH{}{}{}'.format(year,str(month).zfill(2),str(date).zfill(3))
                start_url.append(url)

    def

