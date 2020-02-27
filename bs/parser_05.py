#!/usr/bin/python3
# -*- coding: utf-8 -*-
# sudo apt update
# sudo apt install python-beautifulsoup

from module_05 import *

clear() # чистим экран

txt = get_txt(2) # получить содержимое страницы в виде строки

# print_html('html.txt', txt) # это для контроля

lines = get_content_all(txt)

result = '\n'.join(lines)
print(result) # на экран
print_result('result.txt', result) # в файл
