# -*- coding: utf-8 -*-
import scrapy
from wantedly.items import WantedlyItem
from urllib.parse import urljoin
import re

class ExampleSpider(scrapy.Spider):
    name = 'wantedly'
    allowed_domains = ['wantedly.com']
    start_urls = ['https://www.wantedly.com/projects']

    def parse(self, response):
        for url in response.css('#main-inner .project-title a::attr("href")').extract():

            print(url)
            yield scrapy.Request(urljoin('https://www.wantedly.com',url), self.detail_parse)

        next_page = response.css('.next a::attr("href")').extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page), self.parse)

    def detail_parse(self, response):
        item = WantedlyItem()
        item['title'] = response.css('.project-title ::text').extract_first()
        item['entry'] = response.css('.entry-count.entry-info.left ::text').extract_first()
        item['url'] = response.url
        yield item
