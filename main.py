from newspaper import Article, ArticleException, build
from random import choice


websites = {
    'Onet': 'https://www.onet.pl/',
    'WP': 'https://www.wp.pl/',
    'Interia': 'http://www.interia.pl/',
    'Wyborcza': 'http://wyborcza.pl/',
    'OKO.press': 'https://oko.press/',
    'Dziennik Narodowy': 'http://www.dzienniknarodowy.pl/',
    'Pikio': 'http://pikio.pl/',
    'CNN': 'http://cnn.com/',
    'The Economist': 'http://www.economist.com/'
}


class MyArticle:
    def __init__(self, article, website):
        self.website = website
        self.date = article.publish_date
        self.authors = article.authors
        self.title = article.title
        self.text = article.text


def seek_article():
    while True:
        website = choice(list(websites.keys()))
        urls = build(websites[website]).article_urls()
        if len(urls):
            article = Article(urls[0])
            article.download()
            try:
                article.parse()
            except ArticleException:
                continue
            if len(article.text):
                return MyArticle(article, website)


def brief_article(my_article):
    print('WEBSITE: '+my_article.website)
    print('DATE: '+str(my_article.date))
    print('AUTHOR: '+(my_article.authors[0] if len(my_article.authors) else 'None'))
    print('TITLE: '+my_article.title)
    print('TEXT: '+my_article.text[:200]+'...')


brief_article(seek_article())
