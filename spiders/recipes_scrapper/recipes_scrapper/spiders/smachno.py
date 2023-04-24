from scrapy import Spider, Request
from scrapy.loader import ItemLoader

from recipes_scrapper.items import RecipeItem


class SmachnoSpider(Spider):
    name = 'smachno'

    base_url = 'https://www.smachno.in.ua/'
    start_urls = [
        'https://www.smachno.in.ua/index.php?page=1'
    ]
    pagination_url = 'https://www.smachno.in.ua/index.php'
    page_number = 1

    def parse(self, response):
        if response.status != 200:
            return

        recipes_urls = response.xpath('//div[@class="mini_table"]/a/@href').getall()
        if not recipes_urls:
            return

        for url in recipes_urls:
            yield Request(f"{self.base_url}{url}", callback=self.parse_recipe_page)
        
        self.page_number += 1
        yield Request(f'{self.pagination_url}?page={self.page_number}', callback=self.parse)
    
    def parse_recipe_page(self, response):
        item = ItemLoader(item=RecipeItem(), response=response)
        item.add_xpath('title', '//h1/text()')
        item.add_xpath('ingredients', '//div[@class="ingr"]//li//text()')
        item.add_value('url', response.url)
        return item.load_item()
