import requests, re, os, bs4
from module_05 import *


clear()  # чистим экран
txt = get_txt(2)  # получить содержимое страницы в виде строки

obj_bs = bs4.BeautifulSoup(txt, 'lxml')
list_record = obj_bs.findall('li', class_='channel-schedule__event')
