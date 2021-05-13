import scrapy
from ..items import CrawlallItem

class JobsgoSpider(scrapy.Spider):
    name = 'Jobsgo'
    allowed_domains = ['jobsgo.vn']
    start_urls = ['http://jobsgo.vn/viec-lam-cong-nghe-thong-tin.html']

    def parse(self, response):
        urls = response.xpath('//div[contains(@class, "h3")]/a/@href').getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(
                url=url,
                callback=self.parseJob

            )
        next_page_url = response.xpath(
            '//li[contains(@class, "next")]/a/@href'
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
            '//h1[contains(@class, "media-heading text-semibold")]/text()'
        ).get()

        item['Company_Name'] = response.xpath(
            '//h5[small[contains(@class, "display-block")]]/text()'
        ).get()

        item['Address'] = response.xpath(
            '//div[contains(@class, "data giaphv")]/p/a/text()'
        ).get()

        item['Job_Kind'] = response.xpath(
            '//div[contains(@class, "list")]/a/text()'
        ).getall()

        item['Salary'] = response.xpath(
            '//span[contains(@class, "saraly text-bold text-green")]/text()'
        ).get()

        item['Nature_Work'] = response.xpath(
            '//p[a[contains(@class, "btn btn-xs btn-default")]]/a/text()'
        ).get()

        item['Deadline'] = response.xpath(
            '//span[contains(@class, "deadline text-bold text-orange")]/text()'
        ).get()

        item['Describe'] = response.xpath(
            '//div[h5[contains(text(), "Mô tả công việc")]]/div/p/text()'
        ).getall()

        item['Requirement'] = response.xpath(
            '//div[h5[contains(text(), "Yêu cầu công việc")]]/div/p/text()'
        ).getall()

        item['Benefits'] = response.xpath(
            '//div[h5[contains(text(), "Quyền lợi được hưởng")]]/div/p/text()'
        ).getall()

        yield item

