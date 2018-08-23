# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewtencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称
    name = scrapy.Field()
    # 工作地点
    work_place = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    need_num = scrapy.Field()
    # 职位链接
    position_duty = scrapy.Field()

