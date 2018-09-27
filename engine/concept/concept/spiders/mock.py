# -*- coding: utf-8 -*-
import scrapy

from logging import getLogger

logger = getLogger(__name__)

class MockSpider(scrapy.Spider):
    name = 'mock'
    allowed_domains = ['mock:3000']
    start_urls = ['http://mock:3000/']

    def parse(self, response):
        logger.info(f"...parse {response.url}")
