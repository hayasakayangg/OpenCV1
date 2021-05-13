import scrapy
from ..items import CrawlallItem

class TopcvSpider(scrapy.Spider):
    name = 'topcv'
    allowed_domains = ['topcv.vn']
    start_urls = ['http://topcv.vn/tim-viec-lam-it-phan-mem-c10026/']

    def parse(self, response):
        urls = response.xpath('//h4[contains(@class, "job-title")]/a/@href').getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(
                url=url,
                callback=self.parseJob

            )
        next_page_url = response.xpath(
            '//a[contains(@aria-label, "Next »")]/@href'
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
            '//li[contains(@class, "breadcrumb-item")]/span/text()'
        ).get()[6:]

        item['Company_Name'] = response.xpath(
            '//div[contains(@class, "company-title")]/span/a/text()'
        ).get()

        item['Address'] = response.xpath(
            '//div[contains(@style, "border-bottom: 0px;")]/span/a/text()'
        ).get()

        item['Program_Language'] = response.xpath(
            '//div[h4[contains(text(), "Kỹ năng")]]/span/a/text()'
        ).getall()

        item['Salary'] = response.xpath(
            '//div[strong[contains(text(), "Mức lương: ")]]/span/text()'
        ).get()

        item['Nature_Work'] = response.xpath(
            '//div[strong[contains(text(), "Hình thức làm việc: ")]]/span/text()'
        ).get()

        item['Deadline'] = response.xpath(
            '//div[contains(@class, "content-tab")]/div/div/p/text()'
        ).get()[15:]

        item['Describe'] = response.xpath(
            '//div[contains(@class, "content-tab")]'
        )[0].css('p::text').getall()

        item['Requirement'] = response.xpath(
            '//div[contains(@class, "content-tab")]'
        )[1].css('p::text').getall()

        item['Benefits'] = response.xpath(
            '//div[contains(@class, "content-tab")]'
        )[2].css('p::text').getall()

        yield item

#scrapy shell "https://www.topcv.vn/viec-lam/backend-magento-developer-php/189321.html"