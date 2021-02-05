<div>
<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=blue&style=plastic">
<a href="https://www.python.org/" target="_blank">
<img src="https://img.shields.io/static/v1?label=Made%20with&message=Python&color=blue&style=plastic&logo=PYTHON&logoColor=blue">
</a>
<a href="https://selenium-python.readthedocs.io/" target="_blank">
<img src="https://img.shields.io/static/v1?label=Made%20with&message=Selenium&color=green&style=plastic&logo=Selenium">
</a>
<img src="https://img.shields.io/static/v1?label=Status&message=Em%20andamento&color=yellow&style=plastic&logo=CHECKMARX">
</div>



<h1 align="center">Google Image Downloader </h1>

## Descrição

<p align="justify"> Script para realizar download de imagens do Google automaticamente utilizando Web Scrap</p>

## Tabela de Conteúdos
<!--ts-->
- [Descrição](#descrição)
- [Tabela de Conteúdos](#tabela-de-conteúdos)
- [Features](#features)
- [Pré-requisitos](#pré-requisitos)
- [Como usar](#como-usar)
- [Autor](#autor)


## Features

- [x] Baixar imagens
- [ ] Adaptar para funcionar com Chrome ou Firefox
- [ ] Interface gráfica simples

## Pré-requisitos
Para rodar a aplicação você vai precisar ter instalado as seguintes ferramentas:

* [Python](https://www.python.org/downloads/)
* [Firefox Browser](https://www.mozilla.org/pt-BR/firefox/new/)
* [geckodriver](https://github.com/mozilla/geckodriver/releases)

O geckodriver tem que ser colocado no PATH do Python para funcionar corretamente. 

Após efetuar o download das ferramentas só é preciso instalar as bibliotecas que seram utilizadas, recomendo a criação de um virtual environment para não correr risco das bibliotecas entrarem em conflito com outros projetos. 

```bash
# Clone o repositório
$ git clone <https://github.com/AlexJunior01/Google_Image_Downloader.git>

# Instale as bibliotecas
$ pip install requests

$ pip install Pillow

$ pip install selenium
```

## Como usar
Com as bibliotecas instaladas é só rodar o script, ele irá pedir quatro informações: 

1. Query: termo que ira ser pesquisado no Google para baixar
2. Número de imagens: quantas imagens serão baixadas
3. Nome das imagens: qual nome irá nas imagens, o programa coloca uma numeração na imagem após o nome escolhido
4. Nome da pasta: nome que a pasta criada onde serão salva as imagens

```bash
# Executando o script
$ python3 main.py

# Informações pedidas pelo script
Query:
Número de imagens:
Nome que ira nos arquivos:
Nome da pasta: 
```
---
## Autor

<a href="https://www.linkedin.com/in/alexmomijunior/">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/52081735?s=460&u=2437c208a444d7714f5ba964f364eab5abcb1073&v=4" width="100px;" alt=""/>
 <br/>
 <sub><b>Alex Junior</b></sub></a>
 <br> 



<a href="https://www.linkedin.com/in/alexmomijunior/">
 <img src="https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white">
</a>
<a href="https://alexmomijunior.medium.com/">
 <img src="https://img.shields.io/badge/-Medium-black?style=flat-square&logo=Medium&logoColor=white">
</a>
</a>
<a href="mailto:alexmomijunior@gmail.com">
 <img src="https://img.shields.io/badge/-alexmomijunior@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white">
</a>

---

