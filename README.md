# Projeto WebScraping DataHub Seleção

### Link Projeto
<p align="justify">
https://github.com/flavianoaguiar/python_web_crawling_test
</p>

### Ferramenta e Linguagem
<img src="https://img.shields.io/static/v1?label=python&message=Linguagem &color=grenn&style=for-the-badge&logo=PYTHON"/>
<img src="https://img.shields.io/static/v1?label=beautifulsoup&message=Biblioteca &color=grenn&style=for-the-badge&logo=BEAUTIFULSOUP"/>
<img src="https://img.shields.io/static/v1?label=requests&message=Biblioteca &color=grenn&style=for-the-badge&logo=REQUESTS"/>

### Como Rodar a Aplicação :arrow_forward:

<p align="justify">Instale o Docker</p>

```
https://docs.docker.com/engine/install/ubuntu/
```
<p align="justify">Rodando aplicação</p>

```
docker build -t projeto-scraping
docker run --rm -it -v caminho/absoluto/de/onde/voce/salvou/o/projeto:/app scraping-app

o meu caminho como exemplo =  /home/micael/Área\ de\ Trabalho/projetoDataHub/ProjetoScrapingDataHub

```
<p align="justify">ao rodar o docker run o arquivo proxies.json vai aparacer na pasta de onde você mapeou o volume no meu caso salvou aqui "/home/micael/Área\ de\ Trabalho/projetoDataHub/ProjetoScrapingDataHub"</p>
