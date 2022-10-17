import scrapy


class Posts(scrapy.Spider):
    name="countries"
    allowed_domain=['www.worldometers.info/']
    start_urls=[
        'https://www.worldometers.info/world-population/population-by-country/'
    ]
    def parse(self, response, **kwargs):
        title=response.xpath("//h1/text()").get()
        country=response.xpath("//td/a/text()").getall()

        yield{
            'title':title,
            'county':country
        }
