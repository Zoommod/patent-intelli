import scrapy
import re
import spacy
from asgiref.sync import sync_to_async
from mineracao.models import Empresa, Patente

nlp = spacy.load("pt_core_news_sm")

@sync_to_async
def salvar_no_banco(cnpj_extraido, razao_social_extraida, numero_registro, titulo_patente, resumo_texto):
    empresa, created = Empresa.objects.get_or_create(cnpj = cnpj_extraido, defaults={'razao_social': razao_social_extraida})

    Patente.objects.get_or_create(numero_registro = numero_registro, defaults={'titulo': titulo_patente, 'resumo': resumo_texto, 'empresa': empresa})

class PatentesSpider(scrapy.Spider):
    name = 'patentes'
    start_urls = ['https://example.com']

    async def parse(self, response):
        documento = "A empresa Inovacao Tech, CNPJ 12345678000195, registrou a patente numero BR102030 chamada Algoritmo de Otimizacao Quantica."

        cnpj_match = re.search(r'\d{14}', documento)
        cnpj = cnpj_match.group(0) if cnpj_match else "00000000000000"

        patente_match = re.search(r'BR\d+', documento)
        numero_patente = patente_match.group(0) if patente_match else "Sem registro"

        titulo_match = re.search(r'chamada\s+(.*)\.', documento + ".")
        titulo = titulo_match.group(1).strip() if titulo_match else "Sem título"

        doc = nlp(documento)
        razao_social = "Desconhecida"

        for ent in doc.ents:
            if ent.label_ in ['ORG', 'MISC', 'PER']:
                razao_social = ent.text
                break
        
        if razao_social == "Desconhecida":
            empresa_match = re.search(r'empresa\s+([^,]+)', documento)
            if empresa_match:
                razao_social = empresa_match.group(1).strip()
        

        self.logger.info(f"Dados extraídos - Empresa: {razao_social} | CNPJ: {cnpj} | Patente: {numero_patente}")

        await salvar_no_banco(cnpj_extraido=cnpj, razao_social_extraida=razao_social, numero_registro=numero_patente, titulo_patente=titulo, resumo_texto=documento)

        self.logger.info("Processo de inserção no banco via ORM finalizado.")
    