import requests, re, os, bs4

clear = lambda: os.system('clear')

chanells = {
    1: 'https://tv.yandex.ru/channel/pervyy-16',
    2: 'https://tv.yandex.ru/channel/rossiya-1-31'
}

limits = {
	'time': ('<time class="channel-schedule__time">', '</time>'),
	'text': ('<span class="channel-schedule__text">', '</span>'),
    'title': ('<h1 class="channel-header__text">', '</h1>'),
    'lst': ('<ul class="channel-schedule__list">', '</ul>'),
    'event': ('<li class="channel-schedule__event">', '</li>')
}

def get_txt(num_chanel):
    url = chanells[num_chanel]
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'
    }
    return requests.get(url, headers=head).text

def print_html(name_file, txt):
    f = open(name_file, 'w')
    f.write(txt)  # для контроля выводим в файл
    f.close()
    print('сохранили страницу')

def print_result(name_file, lines):
    file = open(name_file, 'w', encoding='utf-8')
    file.writelines(lines)
    file.close()

def get_content_all(txt):
    obj_bs = bs4.BeautifulSoup(txt, 'lxml')    
    list_record = obj_bs.findall('li', class_ = 'channel-schedule__event')
    lines = []
    mask = r'\d{2}:\d{2}' # это запрос про время
    for item in list_record:
        line = re.search(mask, item)[0]
        lines.append(line)
        
    return lines

