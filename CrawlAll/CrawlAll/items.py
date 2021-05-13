# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlallItem(scrapy.Item):
    Job_Name = scrapy.Field()
    Company_Name = scrapy.Field()
    Address = scrapy.Field()
    Job_Kind = scrapy.Field()
    Salary = scrapy.Field()
    Nature_Work = scrapy.Field()
    Level = scrapy.Field()
    Describe = scrapy.Field()
    Requirement = scrapy.Field()
    Benefits = scrapy.Field()
