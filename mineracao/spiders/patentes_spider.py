import scrapy
import re
import spacy
import pymongo
import datetime
import uuid
from asgiref.sync import sync_to_async
from mineracao.models import Empresa, Patente

nlp = spacy.load("pt_core_news_sm")

@sync_to_async
def salvar_no_banco(cnpj_extraido, razao_social_extraida, numero_registro, titulo_patente, resumo_texto):
    empresa, created = Empresa.objects.get_or_create(cnpj = cnpj_extraido, defaults={'razao_social': razao_social_extraida})

    Patente.objects.get_or_create(numero_registro = numero_registro, defaults={'titulo': titulo_patente, 'resumo': resumo_texto, 'empresa': empresa})

class PatentesSpider(scrapy.Spider):
    name = 'patentes'
    start_urls = ['https://pt.wikipedia.org/wiki/Inova%C3%A7%C3%A3o_tecnol%C3%B3gica']

    def __init__(self, *args, **kwargs):
        super(PatentesSpider, self).__init__(*args, **kwargs)
        self.mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.mongo_client['datalake']
        self.collection = self.db['patentes_raw']

    async def parse(self, response):
        paragrafos = response.css('p::text').getall()

        for paragrafo in paragrafos:
            paragrafo = paragrafo.strip()
        
            if len(paragrafo) < 40:
                continue

            documento_bruto = {
                'html_bruto': paragrafo,
                'url_origem': response.url,
                'data_extracao': datetime.datetime.now()
            }
            self.collection.insert_one(documento_bruto)

            cnpj_match = re.search(r'\d{14}', paragrafo)
            cnpj = cnpj_match.group(0) if cnpj_match else "00000000000000"

            patente_match = re.search(r'BR\d+', paragrafo)
            numero_patente = patente_match.group(0) if patente_match else "Sem registro"

            titulo_match = re.search(r'chamada\s+(.*)\.', paragrafo + ".")
            titulo = titulo_match.group(1).strip() if titulo_match else "Sem título"

            doc = nlp(paragrafo)
            razao_social = "Desconhecida"

            for ent in doc.ents:
                if ent.label_ in ['ORG', 'MISC', 'PER']:
                    razao_social = ent.text
                    break
            
            if razao_social == "Desconhecida":
                empresa_match = re.search(r'empresa\s+([^,]+)', paragrafo)
                if empresa_match:
                    razao_social = empresa_match.group(1).strip()
            

            self.logger.info(f"Dados extraídos - Empresa: {razao_social} | CNPJ: {cnpj} | Patente: {numero_patente}")

            await salvar_no_banco(cnpj_extraido=cnpj, razao_social_extraida=razao_social, numero_registro=numero_patente, titulo_patente=titulo, resumo_texto=paragrafo)

        self.logger.info("Processo de inserção no banco via ORM finalizado.")
