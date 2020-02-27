#!/usr/bin/python3
# -*- coding: utf-8 -*-

from module_04 import *

clear() # чистим экран

txt = get_txt(2) # получить содержимое страницы в виде строки

# print_html('html.txt', txt) # это для контроля

title = get_title(txt)
print(title)

list_pairs = get_content_all(txt) # получить пары значений - название_передачи+время
lines = []
for text, time in list_pairs: # переделать в строки
    lines.append(time + '\t' + text.replace('&quot;', '"'))

result = '\n'.join(lines)
print(result) # на экран
print_result('result.txt', result) # в файл
