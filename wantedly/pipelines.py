# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re


class WantedlyPipeline(object):
    def process_item(self, item, spider):
        item['title'] = re.sub('\s', '',item['title'])
        if item['entry']:
            _entry = re.sub('\s', '',item['entry'])
            item['entry'] = re.search('[0-9]+', _entry).group()
        else:
            item['entry'] = '0'

        return item

