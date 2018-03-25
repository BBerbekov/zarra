from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from crawler.items import ZaraItemLoader, ZaraItem, START_URLS


class ZaraSpider(CrawlSpider):
    name = 'zara'
    allowed_urls = ['https://www.zara.com/us/en']
    start_urls = START_URLS

    rules = [
        Rule(
            LinkExtractor(
                restrict_xpaths=['/html/body/div[2]/section/div/section/div/ul'],
                allow=r'https://www.zara.com/us/en/\S+html\?v1=\d+&v2=\d+'),
            callback='parse_item'
        )
    ]

    def parse_item(self, response):
        selector = Selector(response)
        loader = ZaraItemLoader(ZaraItem(), selector)
        loader.add_value('url', response.url)
        loader.add_xpath('name',  './/*[@id="product"]/div[2]/div/div/header/h1/text()')
        loader.add_xpath('description', './/*[@id="description"]/p/text()')
        loader.add_xpath('size', './/*[@id="product"]/div[2]/div/div/form/fieldset/div/div/label/span/text()')
        loader.add_xpath('photo', ".//*[@id='plain-image']/div/a/img/@src")
        loader.add_xpath('price', './/*[@id="product"]/div[2]/div/div/div[1]/span/text()')
        loader.add_xpath('color', './/*[@id="product"]/div[2]/div/div/p[1]/span/text()')
        return loader.load_item()
