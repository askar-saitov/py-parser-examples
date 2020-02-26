from parser_module import get_txt, print_html, print_result, get_title, get_content

txt = get_txt(1)

# print_html('html.txt', txt) # это для контроля

title = get_title(txt)
lines = get_content(txt)

result = title + '\n' + '\n'.join(lines)

print(result)  # это для контроля
print_result('result.txt', result)