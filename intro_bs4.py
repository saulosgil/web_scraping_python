'''
O módulo BeautifulSoup4 (BS4) é amplamente usado para Web-Scraping.
Instruções completas para instalação podem ser acessadas no site:

http://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Pegando o url
html = urlopen(url='http://pythonscraping.com/pages/page1.html')

# criando um bs objeto
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs) # imprime o bs objeto (que é HTML) 
print(bs.h1) # imprime a tag h1 do bs objecto
print(bs.head) # imprime a tag head do bs objecto
print(bs.div) # imprime a tag div do bs objecto

'''
Repare que a tag extraida esta aninhada em 2 niveis (html -> body -> h1), contudo
é possivel acessar a tag h1 diretamente.
'''
bs
bs.html.body.h1
bs.body.h1
bs.h1

# Outros PARSER - lxml and html5lib
'''
Precisam estar instalados:

$ pip install lxml
$ pip install html5lib

Esses parser são mais flexiveis e lidam melhor com tags mal formatadas como, por exemplo, 
tags sem fechamento, taga aninhadas indevidamente e corpos ausentes.
'''
# bs objeto usando lxml and html5lib
bs = BeautifulSoup(html.read(), 'lxml')
bs = BeautifulSoup(html.read(), 'html5lib')

