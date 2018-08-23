# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newtencent.items import NewtencentItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#']
    pageParse = LinkExtractor(allow=r'start=\d+')
    # 'https://hr.tencent.com/position_detail.php?id=43200&keywords=&tid=0&lid=0'
    # 'https://hr.tencent.com/position_detail.php?id=43202&keywords=&tid=0&lid=0'
    contentParse = LinkExtractor(allow=r'position_detail')

    rules = (
        Rule(pageParse,follow=False),
        Rule(contentParse,callback='parse_item')

    )
    #process_links 参数用于对提取的链接进行选择修改，并返回请求列表
    # def deal_link(self,links):
    #     for each in links:
    #         each.url = 'https://hr.tencent.com/' + str(each.url)
    #     return links

    def parse_item(self, response):

        item = NewtencentItem()
        # 职位名称
        item['name'] = response.xpath('//tr/td[@id="sharetitle"]/text()').extract()[0].split('-')[1]
        # 工作地点
        item['work_place'] = response.xpath('//tr[@class="c bottomline"]/td[1]/text()').extract()[0]
        # 职位类别
        # item['position_type'] = each.xpath('./td[2]/text()').extract()[0]
        item['position_type'] = self.get_position_type(response)
        # 招聘人数
        item['need_num'] = response.xpath('//tr[@class="c bottomline"]/td[3]/text()').extract()[0]
        # 工作职责
        item['position_duty'] = response.xpath('//td[@class="l2"]//li/text()').extract()[0:]

        # item['position_duty'] = info.xpath('string(.)').extract()[0:]

        yield item

    def get_position_type(self,response):
        pos_type = response.xpath('//tr[@class="c bottomline"]/td[2]/text()').extract()
        if len(pos_type):
            pos_type = pos_type[0]
        else:
            pos_type = 'Null'
        return pos_type