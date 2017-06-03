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
    print('TEXT: '+my_article.text[:200]+'.......')


def count_letters(text):
    text = text.lower()
    result = {}
    for letter in text:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result


def how_many_words_can_be_built(word, text):
    letters1 = count_letters(word)
    letters2 = count_letters(text)
    multiplicity = []
    for letter in letters1:
        multiplicity.append(letters2[letter]//letters1[letter])
    return min(multiplicity)


def action():
    article = seek_article()
    brief_article(article)
    count = how_many_words_can_be_built('POSTTRUTH', article.text)
    print('POST-TRUTH INDICATOR: '+str(count))


action()
