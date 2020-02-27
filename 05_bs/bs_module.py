import requests, os
from bs4 import BeautifulSoup
from sys import platform


def clear():
	if platform == "linux" or platform == "linux2":
		os.system('clear')
	elif platform == "win32":
		os.system('cls')
	else:
		pass

chanells = {
    1: 'https://tv.yandex.ru/channel/pervyy-16',
    2: 'https://tv.yandex.ru/channel/rossiya-1-31'
}

def get_txt(num_chanel):
    url = chanells[num_chanel]
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'
    }
    return requests.get(url, headers=head).text

def print_result(name_file, lines):
	with open(name_file, 'w', encoding='utf-8') as f:
		f.writelines(lines)
