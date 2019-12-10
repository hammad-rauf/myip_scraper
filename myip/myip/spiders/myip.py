from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import MyipItem

import random

class MyipSpider(CrawlSpider):

    name = "myip"

    start_urls = ["https://myip.ms/browse/sites/1/ownerID/376714/ownerID_A/1"]

    # rules = (
    #     Rule(LinkExtractor(restrict_css=('a[href^="/browse/sites/"]')),callback="parsee"),
    # )


    def __init__(self):

        self.list = []

        for count in range(3063):
            self.list.append(count) 

        #self.proxy_pool = ['https://24.172.82.94:53281','https://98.190.180.62:8080','https://24.172.82.94:53281']


        self.pointer = 2

    def parse(self, response):  

        product = MyipItem()

        #print(self.pointer)

        names = response.css(".row_name a::text").extract()
        ratings = response.css("td+ td .grey::text").extract()
        visiters = response.css(".sval .grey::text").extract()

        for name, rating, visiter in zip(names,ratings,visiters):
            product['name'] = name
            
            rating = str(rating)
            rating = rating.split('#')[1]
            rating = rating.replace(',','')
            product['rating'] = rating

            visiter = visiter.replace(',','')            
            product['visiter'] = visiter
            
            yield product


        temp_links = response.css('a[href^="/browse/sites/"]::attr(href)').extract()

        links = []

        for link in temp_links:

             if f"/browse/sites/{self.pointer}" in link:
                 links.append(link)
                 self.pointer += 1

        #meta={'proxy': random.choice(self.proxy_pool)},
        
        for next_page in links:
            yield response.follow(next_page, callback= self.parse)
