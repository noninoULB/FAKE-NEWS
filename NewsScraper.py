import feedparser as fp
import json
import newspaper
from newspaper import Article
from time import mktime
from datetime import datetime

# Set the limit for number of articles to download
LIMIT = 4000
label = "FAKE"

file = open('fake_real_news.csv', 'a', encoding='utf-8')

data = {}
data['newspapers'] = {}

LINKS = ['https://www.thedailymash.co.uk/', 'http://www.thecivilian.co.nz/', 'https://www.thespoof.com/',
         'https://www.thebeaverton.com/', 'https://www.newyorker.com/humor/borowitz-report', 'https://www.theonion.com/' ]

reallinks = ['http://edition.cnn.com/', 'http://www.bbc.com/', 'https://www.theguardian.com/international', 
             'http://www.foxnews.com/', 'http://www.nbcnews.com/', 'https://www.washingtonpost.com/'  ]

LINKS = reallinks
label = "REAL"

count = 1
id_ = 0

# Iterate through each news company
for link in LINKS:

    paper = newspaper.build(link, memoize_articles=False)

    noneTypeCount = 0
    for content in paper.articles:
        if count > LIMIT:
            break
        try:
            content.download()
            content.parse()
        except Exception as e:
            print(e)
            print("continuing...")
            continue
        # Again, for consistency, if there is no found publish date the article will be skipped.
        # After 10 downloaded articles from the same newspaper without publish date, the company will be skipped.
        if content.publish_date is None:
            print(count, " Article has date of type None...")
            noneTypeCount = noneTypeCount + 1
            if noneTypeCount > 10:
                print("Too many noneType dates, aborting...")
                noneTypeCount = 0
                break
            count = count + 1
            continue
        
        body = content.text
        body = body.replace("\n", "")

        string = str(id_) + ';' + content.title + ';"' + content.text + '";' + label + "\n"
        id_ += 1
        file.write(string)

file.close()
