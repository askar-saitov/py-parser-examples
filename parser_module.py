import requests

chanells = {
    1: 'https://tv.yandex.ru/channel/pervyy-16',
    2: 'https://tv.yandex.ru/channel/pervyy-16'
}

limits = {
	'time': ('<time class="channel-schedule__time">', '</time>'),
	'content': ('<span class="channel-schedule__text">', '</span>'),
    'title': ('<h1 class="channel-header__text">', '</h1>')
}

def get_txt(num_chanel):
    url = chanells[num_chanel]
    head = { 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
    }
    return requests.get(url, headers=head).text

def print_html(name_file, txt):
    f = open(name_file, 'w')
    f.write(txt)  # для контроля выводим в файл
    f.close()
    print('сохранили страницу')

def print_result(name_file, lines):
    '''
    пишем линии в файл
    '''
    file = open('result.txt', 'w', encoding='utf-8')
    file.writelines(lines)
    file.close()

def get_title(txt):
    '''
    ищем название канала
    '''
    pos = 0
    lim_left, lim_right = limits['title']
    posLeft = txt.find(lim_left, pos) + len(lim_left)
    posRight = txt.find(lim_right, posLeft)
    return txt[posLeft:posRight].replace('&quot;', '"')

def get_content(txt):
    pos = 0
    lines = []
    while txt.find(limits['time'][0], pos) >= 0:
    	clmns = []
    	for item in ['time','content']:
            lim_left, lim_right = limits[item]
            posLeft = txt.find(lim_left, pos) + len(lim_left)
            posRight = txt.find(lim_right, posLeft)
            clmn = txt[posLeft:posRight].replace('&quot;', '"')
            pos = posRight
            clmns.append(clmn)
    	line = clmns[0] + '\t' + clmns[1]
    	lines.append(line)
    return lines

