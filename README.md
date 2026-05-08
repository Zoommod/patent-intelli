# Sistema de Inteligência de Patentes

Sistema automatizado para mineração, extração e análise de informações de patentes utilizando web scraping, processamento de linguagem natural e APIs REST.

## 🚀 Funcionalidades

- **Coleta Automática**: Web scraping de patentes da Wikipedia utilizando Scrapy
- **Processamento de Linguagem Natural**: Extração de entidades (empresas) usando spaCy com modelo pt_core_news_sm
- **Extração de Informações**: Identificação automática de CNPJ, número de registro, título e resumo de patentes
- **Data Lake**: Armazenamento de dados brutos no MongoDB
- **API REST**: Endpoints para consulta de empresas e patentes com busca e filtros
- **Agendamento Automático**: Tarefas agendadas via Celery Beat para coleta periódica
- **Painel Administrativo**: Interface do Django Admin para gerenciamento dos dados

## 🛠 Tecnologias Utilizadas

- **Backend**: Django 6.0.4
- **API Framework**: Django REST Framework 3.17.1
- **Processamento Assíncrono**: Celery 5.6.3 com Redis
- **Web Scraping**: Scrapy 2.15.0
- **Processamento de Linguagem Natural**: spaCy 3.8.13 (pt_core_news_sm)
- **Banco de Dados Principal**: SQLite (desenvolvimento) / PostgreSQL (recomendado para produção)
- **Data Lake**: MongoDB
- **Message Broker**: Redis / Valkey

