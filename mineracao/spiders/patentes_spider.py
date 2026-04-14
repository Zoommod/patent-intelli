import scrapy

class PatentesSpider(scrapy.Spider):
    name = 'patentes'
    start_urls = ['https://example.com']

    def parse(self, response):
        self.logger.info("Acessando a página e iniciando a varredura!")