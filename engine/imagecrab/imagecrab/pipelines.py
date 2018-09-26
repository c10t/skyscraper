# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime

import scrapy

from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.misc import md5sum


# custom images pipeline
# see https://doc.scrapy.org/en/latest/topics/media-pipeline.html
class ImagecrabPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for url in item['urls']:
            yield scrapy.Request(url, meta={
                'directory': item['directory']
                })

    def image_downloaded(self, response, request, info):
        checksum = None
        for path, image, buf in self.get_images(response, request, info):
            if checksum is None:
                buf.seek(0)
                checksum = md5sum(buf)
            width, height = image.size
            prefix = datetime.now().strftime('%Y%m%d_')
            filename = prefix + request._url.rsplit("/", 1)[1]
            path = f"{response.meta['directory']}/{filename}"
            self.store.persist_file(path, buf, info,
                                    meta={'width': width, 'height': height})  
        return checksum
