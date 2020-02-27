from bs_module import *

clear()  # чистим экран

print('+++++++++++++++++++++++++++')

txt = get_txt(2)  # получить содержимое страницы в виде строки
bs = BeautifulSoup(txt, 'lxml')

lines = []

title = bs.find('h1', class_='channel-header__text').contents[0]
lines.append(title)

list_li = bs.find_all('li', class_='channel-schedule__event')
for li in list_li:
	time = li.find('time', class_='channel-schedule__time').contents[0]
	name = li.find('span', class_='channel-schedule__text').contents[0]
	line = '%s\t%s' % (time, name)
	lines.append(line)

result = '\n'.join(lines)

print(result) # для контроля на экран
print_result("bs_result.txt", result)

print('--------------------------')
