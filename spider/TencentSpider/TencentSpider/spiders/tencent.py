#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
# 导入CrawlSpider类和Rule
from scrapy.spiders import CrawlSpider, Rule
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.linkextractors import LinkExtractor
from TencentSpider.items import TencentItem

class TencentSpider(CrawlSpider):
    name = "tencent"
    allow_domains = ["hr.tencent.com"]
    start_urls = ["http://hr.tencent.com/position.php?&start=0#a"]

    # Response里链接的提取规则，返回的符合匹配规则的链接匹配对象的列表
    # pagelink = LinkExtractor(allow=r"php?id=\d+")

    rules = [
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        # Rule(LinkExtractor(allow=r"start=\d+"), process_links='deal_link',callback = "parseTencent",)
        Rule(LinkExtractor(allow=r"position_detail"),callback = "parseTencent",)
    ]

    # def deal_link(self,links):
    #     for each in links:
    #         each.url = 'https://hr.tencent.com/' + str(each.url)
    #     return links

    # 指定的回调函数
    def parseTencent(self, response):
        # print response.url
        #evenlist = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        #oddlist = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        #fulllist = evenlist + oddlist
        #for each in fulllist:
        # for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
        item = TencentItem()
        # 职位名称
        item['name'] = response.xpath('//tr/td[@id="sharetitle"]/text()').extract()[0]
        # 工作地点
        item['work_place'] = response.xpath('//tr[@class="c bottomline"]/td[1]/text()').extract()[0]
        # 职位类别
        # item['position_type'] = each.xpath('./td[2]/text()').extract()[0]
        # item['position_type'] = self.get_position_type(response)
        # 招聘人数
        item['need_num'] = response.xpath('//tr[@class="c bottomline"]/td[3]/text()').extract()[0]
        # 工作职责
        item['position_duty'] = response.xpath('//td[@class="l2"]//li/text()').extract()[0]

        yield item