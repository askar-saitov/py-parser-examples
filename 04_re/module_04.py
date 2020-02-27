import requests, re, os

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
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'
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
    file = open(name_file, 'w', encoding='utf-8')
    file.writelines(lines)
    file.close()

def get_title(txt):
    '''
    ищем название канала
    '''
    left, right = limits['title']
    mask = '(?<=' + left + ').*?(?=' + right + ')'
    line = re.search(mask, txt)[0] # первое вхождение
    return line

def get_content_time(txt):
    '''
    префикс r нужен для обработки сырых строк
    чтобы обратный слеш не экранировал символы
    '''
    mask = r'\d{2}:\d{2}' # это запрос про время
    # line = re.search(mask, txt)[0] # первое вхождение
    # return line
    lines = re.findall(mask, txt) # найти все вхождения
    return lines

def get_content_text(txt):
    left, right = limits['text']
    mask = '(?<=' + left + ').*?(?=' + right + ')'
    lines = re.findall(mask, txt) # найти все вхождения
    return lines

def get_content_all(txt):
    left, right = limits['lst']
    mask = '(?<=' + left + ').*?(?=' + right + ')'
    content = re.search(mask, txt)[0] # первое вхождение
    # print(content)
    lines_time = get_content_time(content)
    lines_text = get_content_text(content)
    lines = []
    for i in range(len(lines_text)):
        lines.append((str(lines_text[i]), str(lines_time[i])))
    return lines


