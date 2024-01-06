
'''
Scraping test - 
Page - http://pythonscraping.com/pages/page1.html
'''

# Bib
from urllib.request import urlopen

# Getting url and printing 
html = urlopen(url='http://pythonscraping.com/pages/page1.html')
print(html.read())
