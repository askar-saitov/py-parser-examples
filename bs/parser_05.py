#!/usr/bin/python3
# -*- coding: utf-8 -*-
# sudo apt update
# sudo apt install python-beautifulsoup

from module_05 import *
from lxml import html

clear() # чистим экран

txt = get_txt(2) # получить содержимое страницы в виде строки

tree = html.fromstring(txt)
lines = tree.xpath('//li')  # все li теги
print(str(lines[0]))
print('\n'.join(lines))
film_list = soup.find('div', {'class': 'profileFilmsList'})



# print_html('html.txt', txt) # это для контроля
# print('++++++')
# lines = get_content_all(txt)

# result = '\n'.join(lines)
# print(result) # на экран
# print_result('result.txt', result) # в файл
# print('The end')
