# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import MySQLdb


class WantedlyPipeline(object):
    def process_item(self, item, spider):
        item['title'] = re.sub('\s', '',item['title'])
        item['id'] = re.search('[0-9]+',item['url']).group(0)
        if item['entry']:
            _entry = re.sub('\s', '',item['entry'])
            item['entry'] = re.search('[0-9]+', _entry).group()
        else:
            item['entry'] = '0'


        return item

class MySQLPipeline(object):
    def open_spider(self, spider):
        settings = spider.settings
        params = {
            'host': settings.get('MYSQL_HOST', 'localhost'), # ホスト
            'db': settings.get('MYSQL_DATABASE', 'scraping'), # DB名
            'user': settings.get('MYSQL_USER', ''),
            'passwd': settings.get('MYSQL_PASSWORD', ''),
            'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),
        }
        self.conn = MySQLdb.connect(**params)
        self.c = self.conn.cursor()

        # self.c.execute('DROP TABLE IF EXISTS wantedly_items')

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS wantedly_items (
            id INT UNSIGNED,
            url TEXT,
            entry INT UNSIGNED,
            title TEXT,
            PRIMARY KEY(id)
            )
        ''')
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):

        self.c.execute('''
                      INSERT INTO wantedly_items VALUES (%s, %s, %s, %s)''',
                       (item['id'],
                        item['url'],
                        item['entry'],
                        item['title']
                        ))
        self.conn.commit()
        return item
