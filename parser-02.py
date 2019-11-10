import requests

url = 'https://tv.yandex.ru/50/channels/265'
head = { 
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
txt = requests.get(url, headers=head).text

f = open('html.txt', 'w')
f.write(txt)  # для контроля выводим в файл
f.close(); print('сохранили страницу')

limits = [
	'<time class="channel-schedule__time">',
	'</time>',
	'<span class="channel-schedule__text">',
	'</span>'
]

pos = 0
lines = []
while txt.find(limits[0], pos) >= 0:
	clmns = []
	for i in range(2):
		posLeft = txt.find(limits[i*2], pos) + len(limits[i*2])
		posRight = txt.find(limits[i*2+1], posLeft)
		clmn = txt[posLeft:posRight].replace('&quot;', '"')
		pos = posRight
		clmns.append(clmn)

	line = clmns[0] + '\t' + clmns[1]
	print(line)  # это для контроля
	lines.append(line + '\n')

file = open('result.txt', 'w', encoding='utf-8')
file.writelines(lines)  # пишем линии в файл
file.close()
