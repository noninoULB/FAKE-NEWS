
import newspaper
from random import randint

file = open('fake_real_news.csv', 'w', encoding='utf-8')
header = ",title,text,label\n"

real_news_links = ['http://cnn.com', 'https://www.thetimes.co.uk/', 'https://www.theguardian.com/us',
				   'https://aeon.co/', 'https://www.dailymail.co.uk/home/index.html', 'https://www.bbc.com/news']

fake_news_link = ['https://www.thedailymash.co.uk/', 'http://www.thecivilian.co.nz/', 'https://www.thespoof.com/',
                  'https://www.thebeaverton.com/', 'https://www.newyorker.com/humor/borowitz-report', 'https://www.theonion.com/' ]

current = 0
number = 4000

titles = []

while(current < number):

	for link in real_news_links:

		paper = newspaper.build(link)

		for article in paper.articles:

			try:
				article.download()
				article.parse()

				id_   = str(current)
				title = article.title
				body  = article.text[:]
				label = 'REAL'

				if(len(body) > 6000 and title not in titles):
					titles.append(title)
					string = id_ + "," + title + ',"' + body + '",' + label + "\n"
					file.write(string)
					current += 1

			except:
				continue

del(titles)

current = 4000
number = 8000

titles = []

while(current < number):

	for link in fake_news_link:

		paper = newspaper.build(link)

		for article in paper.articles:

			try:
				article.download()
				article.parse()

				id_   = str(current)
				title = article.title
				body  = article.text[:]
				label = 'FAKE'

				if(len(body) > 6000 and title not in titles):
					titles.append(title)
					string = id_ + "," + title + ',"' + body + '",' + label + "\n"
					file.write(string)
					current += 1

			except:
				continue

del(titles)

file.close()




