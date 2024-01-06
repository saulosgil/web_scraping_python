'''
The modulo BeautifulSoup4 (BS4) is commonly used for Web-Scraping.
Complete instructions to install are in http://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Getting url
html = urlopen(url='http://pythonscraping.com/pages/page1.html')

# bs object
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs) # print of the bs object (that is HTML) 
print(bs.h1) # print of the tag h1 of the bs object
print(bs.head) # print of the tag head of the bs object 
print(bs.div) # print of the tag div of the bs object 

'''
Observe that extracted tag is nested in 2 levels (html -> body -> h1), but  it is
possible to acess h1 directly.
'''
bs
bs.html.body.h1
bs.body.h1
bs.h1

# OTHERs PARSER - lxml and html5lib
'''
It is necessary to install:

$ pip install lxml
$ pip install html5lib

These parser are more flexible for unformmated tags (e.g., tags without closed)
'''
# bs object using lxml and html5lib
bs = BeautifulSoup(html.read(), 'lxml')
bs = BeautifulSoup(html.read(), 'html5lib')

