import scrapy
from ..items import CrawlallItem
class CareerlinkSpider(scrapy.Spider):
    name = 'careerlink'
    allowed_domains = ['careerlink.vn']
    start_urls = ['http://careerlink.vn/viec-lam/nhan-vien-it/']

    def parse(self, response):
        urls = response.xpath(
            '//a[contains(@class, "job-link clickable-outside")]/@href'
        ).getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(
                url=url,
                callback=self.parseJob

            )
        next_page_url = response.xpath(
            '//a[contains(@rel, "next")]/@href'
        ).get()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(
                url=next_page_url,
                callback=self.parse
            )

    def parseJob(self, response):
        item = CrawlallItem()
        item['Job_Name'] = response.xpath(
            '//h1[contains(@class, "h4 job-title text-primary font-weight-bolder")]/text()'
        ).get()[1:-1]

        item['Company_Name'] = response.xpath(
            '//p[contains(@class, "org-name mb-2")]/a/span/text()'
        ).get()

        item['Address'] = response.xpath(
            '//span[contains(@itemprop, "addressRegion")]/text()'
        ).get()[1:-1]

        item['Job_Kind'] = response.xpath(
            '//div[contains(@class, "job-summary-item d-flex d-lg-block")]/div'
        )[11].css('a').css('span::text').getall()

        item['Salary'] = response.xpath(
            '//span[contains(@itemprop, "value")]/text()'
        ).get()[1:-1]

        item['Nature_Work'] = response.xpath(
            '//div[contains(@itemprop, "employmentType")]/text()'
        ).get()[10:][1:-1]

        item['Level'] = response.xpath(
            '//div[contains(@itemprop, "qualifications")]/text()'
        ).get()[1:-1]

        item['Deadline'] = response.xpath(
            '//div[contains(@class, "d-flex flex-wrap mt-2")]/div/text()'
        )[4].get()[1:-1]

        item['Describe'] = response.xpath(
            '//div[contains(@itemprop, "description")]'
        )[0].css('p::text').getall()

        item['Requirement'] = response.xpath(
            '//div[contains(@itemprop, "skills")]'
        )[0].css('p::text').getall()

        yield item
