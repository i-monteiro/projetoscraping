# projetoscraping
Para rodar o web scraping, execute o comando abaixo dentro da pasta coleta:

```bash
scrapy crawl mercadolivre -o ../../data/data.json
```

Para rodar o código de transformação dos dados, execute o comando abaixo dentro da pasta SRC:

```bash
python transformacao/main.py
```