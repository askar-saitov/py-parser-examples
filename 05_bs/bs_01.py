'''
pip3 install BeautifulSoup
pip3 install lxml
'''

from bs4 import BeautifulSoup
from sys import platform
import os

def clear():
	if platform == "linux" or platform == "linux2":
		os.system('clear')
	elif platform == "win32":
		os.system('cls')
	else:
		pass

clear()  # чистим экран

print('+++++++++++++++++++++++++++')

name_file = 'index.html' # файл заранее создали и положили рядом

with open(name_file, 'r') as f:
	contents = f.read()
	soup = BeautifulSoup(contents, 'lxml')
	print(soup.h2)
	print(soup.head)
	print(soup.li)
	print(soup.li.contents[0])

print('--------------------------')
