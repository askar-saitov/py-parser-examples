from bs_module import *
import re

clear()  # чистим экран

print('+++++++++++++++++++++++++++')

contents = get_txt(2)  # получить содержимое страницы в виде строки

bs = BeautifulSoup(contents, 'lxml')

list_li = bs.find_all('li', class_='channel-schedule__event')
mask = r'\d{2}:\d{2}'
for li in list_li:
	line = re.search(mask, str(li))[0]
	print(line)

print('--------------------------')
