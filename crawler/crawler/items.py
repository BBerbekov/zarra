# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join

START_URLS = ['https://www.zara.com/us/en/woman-new-in-l1180.html',
              'https://www.zara.com/us/en/woman-outerwear-l1184.html?v1=719012',
              'https://www.zara.com/us/en/woman-jackets-l1114.html?v1=358002',
              'https://www.zara.com/us/en/woman-blazers-l1055.html?v1=797504',
              'https://www.zara.com/us/en/woman-dresses-l1066.html?v1=719020',
              'https://www.zara.com/us/en/woman-jumpsuits-l1150.html?v1=399001',
              'https://www.zara.com/us/en/woman-shirts-l1217.html?v1=719021',
              'https://www.zara.com/us/en/woman-body-l1057.html?v1=602501',
              'https://www.zara.com/us/en/woman-trousers-l1335.html?v1=719022',
              'https://www.zara.com/us/en/woman-trousers-l1335.html?v1=719022',
              'https://www.zara.com/us/en/woman-trousers-shorts-l1355.html?v1=949510',
              'https://www.zara.com/us/en/woman-jeans-l1119.html?v1=719019',
              'https://www.zara.com/us/en/woman-skirts-l1299.html?v1=719016',
              'https://www.zara.com/us/en/woman-knitwear-l1152.html?v1=719015',
              'https://www.zara.com/us/en/woman-tshirts-l1362.html?v1=719014',
              'https://www.zara.com/us/en/woman-sweatshirts-l1320.html?v1=364001',
              'https://www.zara.com/us/en/woman-beachwear-l1052.html?v1=398505',
              'https://www.zara.com/us/en/woman-shoes-l1251.html?v1=719531',
              'https://www.zara.com/us/en/woman-bags-l1024.html?v1=819022',
              'https://www.zara.com/us/en/woman-accessories-l1003.html?v1=358026',
              'https://www.zara.com/us/en/woman-trend-8-l1332.html?v1=940529',
              'https://www.zara.com/us/en/woman-suits-l1437.html?v1=815545',
              'https://www.zara.com/us/en/woman-trend-5-l1329.html?v1=821006'
              ]


class ZaraItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    size = scrapy.Field()
    color = scrapy.Field()
    photo = scrapy.Field()
    price = scrapy.Field()
    id_product = scrapy.Field


class ZaraItemLoader(ItemLoader):
    url_out = TakeFirst()
    name_out = TakeFirst()
    description_in = Join()
    description_out = TakeFirst()
    size_in = Join()
    size_out = TakeFirst()
    photo_out = TakeFirst()
    color_out = TakeFirst()
    price_in = Join()
    price_out = TakeFirst()
    id_product_out = TakeFirst()
