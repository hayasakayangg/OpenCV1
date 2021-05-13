import scrapy
from ..items import CrawlallItem

class Vieclam1Spider(scrapy.Spider):
    name = 'Vieclam1'
    allowed_domains = ['careerbuilder.vn']
    start_urls = ['http://careerbuilder.vn/viec-lam/cntt-phan-mem-c1-trang-1-vi.html/']

    def parse(self, response):
        urls = response.xpath('//a[contains(@class, "job_link")]/@href').getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(
                url=url,
                callback=self.parseJob

            )
        next_page_url = response.xpath(
            '//li[contains(@class, "next-page")]/a/@href'
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
            '//h1[contains(@class, "title")]/text()'
        ).get()

        item['Company_Name'] = response.xpath(
            '//a[contains(@class, "employer job-company-name")]/text()'
        ).get()

        item['Address'] = response.xpath(
            '//div[contains(@class, "map")]/p/a/text()'
        ).get()

        item['Job_Kind'] = response.xpath(
            '//li[strong[em[contains(@class, "mdi mdi-briefcase")]]]/p/a/text()'
        ).getall()

        item['Salary'] = response.xpath(
            '//li[strong[i[contains(@class, "fa fa-usd")]]]/p/text()'
        ).get()

        item['Level'] = response.xpath(
            '//li[strong[i[contains(@class, "mdi mdi-account")]]]/p/text()'
        ).get()

        item['Form'] = response.xpath(
            '//li[strong[em[contains(@class, "mdi mdi-briefcase-edit")]]]/p/text()'
        ).get()

        item['Deadline'] = response.xpath(
            '//li[strong[i[contains(@class, "mdi mdi-calendar-check")]]]/p/text()'
        ).get()

        item['Describe'] = response.xpath(
            '//div[h3[contains(text(), "Mô tả Công việc")]]/p/text()'
        ).getall()

        item['Requirement'] = response.xpath(
            '//div[h3[contains(text(), "Yêu Cầu Công Việc")]]/p/text()'
        ).getall()

        yield item

