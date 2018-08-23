# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TctSpider(scrapy.Spider):
    name = 'tct'
    allowed_domains = ['hr.tencent.com']
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        node_links = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for each in node_links:
            item = TencentItem()
            # 职位名称
            item['name'] = each.xpath('./td[1]/a/text()').extract()[0]
            # 工作地点
            item['work_place'] = each.xpath('./td[4]/text()').extract()[0]
            # 职位类别
            # item['position_type'] = each.xpath('./td[2]/text()').extract()[0]
            item['position_type'] = self.get_position_type(response)
            # 招聘人数
            item['need_num'] = each.xpath('./td[3]/text()').extract()[0]
            # 职位链接
            item['position_url'] = each.xpath('./td[1]/a/@href').extract()[0]
            # 发布时间
            item['release_time'] = each.xpath('./td[5]/text()').extract()[0]

            yield item
        if self.offset<3510:
            self.offset += 10
        yield scrapy.Request(self.url + str(self.offset),callback = self.parse)

    def get_position_type(self,response):
        pos_type = response.xpath('//tr[@class="even"]//td[2]/text() |//tr[@class="odd"]//td[2]/text()').extract()
        if len(pos_type):
            pos_type = pos_type[0]
        else:
            pos_type = 'Null'
        return pos_type