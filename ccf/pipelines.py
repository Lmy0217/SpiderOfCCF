# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class CcfPipeline(object):
    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):  # 关闭时自动调用
        f = open('papers.json', 'w')
        f.write(json.dumps(spider.papers))
        f.close()