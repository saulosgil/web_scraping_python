# Conectando de forma confiável e tratando exceções
'''

'''
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


url_certo = 'http://pythonscraping.com/pages/page1.html'
url_errado = 'http://pythonscraping.com/pages/pages1.html' # tem um s a mais no page"s"

# testando o tratamento do erro de URL
## URL certo
try:
  html = urlopen(url_certo)
except HTTPError as e:
  print(e)
except URLError as e:
  print(e)
else:
  print('It worked!')

## URL errado
try:
  html = urlopen(url_errado)
except HTTPError as e:
  print(e)
except URLError as e:
  print(e)
else:
  print('It worked!')

# Exemplo de função para tratar distintos erros 
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
  # trata erro de url
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
    #trata erro de atributo (caso não encontre a tag h1 [None])
  try:
    bs = BeautifulSoup(html.read(), 'html.parser')
    title = bs.h1
  except AttributeError as e:
    return None
  return title

# usando a função para pegar o titulo
## usando a url certa (retorna o titulo)
title = getTitle(url_certo)
if title == None:
  print('Title could not be found')
else:
  print(title)

## usando a url certa
title = getTitle(url_errado)
if title == None:
  print('Title could not be found')
else:
  print(title)
