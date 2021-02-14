from bs4 import BeautifulSoup
import requests


def articleParsing(page):
	# Parsing div {class: mw-parser-output}
	print('-' * 50)
	for p in page.find('div', {'class': 'mw-parser-output'}).findAll('p'):
		print(p.text)
	print('-' * 50)
	return 'I\'m choosing the next article'
