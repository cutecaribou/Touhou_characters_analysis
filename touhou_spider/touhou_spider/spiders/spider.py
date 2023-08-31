import scrapy

# паук, который собирает имена и ссылки на страницы каждого персонажа
class TouhouSpider(scrapy.Spider):
    name = 'touhou_characters'
    allowed_domains = 'touhou.fandom.com'
    start_urls = ['https://touhou.fandom.com/wiki/Category:Characters']

    def parse(self, response):
        # список всех персонажей
        characters = response.xpath('//li[@class="category-page__member"]')

        for member in characters:
            yield {
                'name' : member.xpath('.//a[@class="category-page__member-link"]/text()').get(),
                'url' : member.xpath('.//a[@class="category-page__member-link"]/@href').get()
            }