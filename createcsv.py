

file = open('fake_real_news.csv', 'a', encoding='utf-8')
header = ";title;text;label\n"

file.write(header)
file.close()