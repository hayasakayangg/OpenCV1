import scrapy
from ..items import CrawlallItem

class Timviec365Spider(scrapy.Spider):
    name = 'timviec365'
    allowed_domains = ['timviec365.vn']
    start_urls = ['http://timviec365.vn/viec-lam-it-phan-mem-c13v0/']

    def parse(self, response):
        urls = response.xpath('//a[contains(@class, "title_cate")]/@href').getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(
                url=url,
                callback=self.parseJob

            )
        next_page_url = response.xpath(
            '//a[contains(@title, "Next page")]/@href'
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
            '//div[contains(@class, "right_tit")]/h1/text()'
        ).get()

        item['Company_Name'] = response.xpath(
            '//p[contains(@class, "h2")]/a/text()'
        ).get()

        item['Address'] = response.xpath(
            '//p[contains(@class, "dd_tuyen")]/a/text()'
        )[0].getall()

        item['Job_Kind'] = response.xpath(
            '//div[contains(@class, "form_control ic8")]'
        )[0].css('a::text').getall()

        item['Salary'] = response.xpath(
            '//p[contains(@class, "lv_luong")]/span/text()'
        ).get()

        item['Nature_Work'] = response.xpath(
            '//div[contains(@class, "form_control ic4")]/span/text()'
        ).get()

        item['Level'] = response.xpath(
            '//div[contains(@class, "form_control ic2")]/span/text()'
        ).get()

        item['Describe'] = response.xpath(
            '//div[contains(@class, "box_mota")]/text()'
        ).getall()

        item['Requirement'] = response.xpath(
            '//div[contains(@class, "box_yeucau")]/text()'
        ).getall()

        item['Benefits'] = response.xpath(
            '//div[contains(@class, "box_quyenloi")]/text()'
        ).getall()

        yield item
