import scrapy


class MyipItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    rating = scrapy.Field()
    visiter = scrapy.Field()

    pass
