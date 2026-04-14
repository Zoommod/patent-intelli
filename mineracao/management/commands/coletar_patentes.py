from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from mineracao.spiders.patentes_spider import PatentesSpider

class Command(BaseCommand):
    help = 'Inicia o processo de coleta e extração de patentes'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Gatilho acionado: O rôbo de extração começará a rodar aqui."))

    process = CrawlerProcess()
    process.crawl(PatentesSpider)
    process.start()