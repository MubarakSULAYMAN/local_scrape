import requests
from bs4 import BeautifulSoup as soup


def scrape_legit():

    news_url = "https://www.legit.ng/tag/kwara-state-news-today.html"
    source = "Naij.com > Legit.ng" 
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("article", {"class" : "c-article-card-no-border"})

    legit_news = []

    for container in containers:
        headline = container.span.getText().strip()
        date = container.div.time.getText().strip()
        image = container.a.picture.img["data-src"]
        address = container.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        author = str(page_soup.body.find(class_="c-article-info__author").getText().strip())
        post = str(page_soup.body.find(class_="l-article__body c-article__body"))
            
        weeds = ["READ ALSO:", "NAIJ.com upgrades to Legit.ng: a letter from our Editor-in-Chief Bayo Olupohunda",
                 "PAY ATTENTION:", "Download our mobile app to enjoy the latest news updates",  "<a>", "</a>"]
        
        for weed in weeds:
            post = post.replace(weed, "\n")

#         a_tag = page_soup.body.find(class_="l-article__body c-article__body").a["href"]
#         new_post = post.replace(a_tag, "\n")

        news_read = soup(post, "html.parser")
        
        row = {"source": str(source),
            "headline": str(headline),
            "address": str(address),
            "date": str(date),
            "image": str(image),
            "author": str(author),
            "news_read": str(news_read)
            }
        legit_news.append(row)
                
    return legit_news


def scrape_kwaralefro():
    news_url = "http://www.kwaralefro.com"
    source = "Kwara Legacy Frontier"
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("div", {"class": "content-excerpt"})

    kwaralefro_news = []

    for container in containers:
        headline = container.h1.a.get_text().strip()
        date = container.div.span.a.time.get_text().strip()
        image = container.a.img["src"]
        address = container.div.p.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        author = container.span.span.a.get_text().strip()
        post = str(page_soup.body.find(class_="entry clearfix"))
        news_read = soup(post, "html.parser")

        row = {
        "source": str(source),
        "headline": str(headline),
        "address": str(address),
        "author": str(author),
        "date": str(date),
        "image": str(image),
        "news_read": str(news_read)
        }
        kwaralefro_news.append(row)

    return kwaralefro_news


def scrape_todayng():
    news_url = "https://www.today.ng/topic/kwara"
    source = "today.ng"
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("div", {"class": "td_module_11"})

    today_ng_news = []
    for container in containers:
        headline = container.find(class_="entry-title td-module-title").get_text().strip()
        image = container.div.a.img["src"]
        address = container.div.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        date = str(page_soup.body.find(class_="entry-date updated td-module-date").get_text().strip())
        author = str(page_soup.body.find(class_="td-post-author-name").get_text().strip())
        post = str(page_soup.body.find(class_="td-post-content"))

        # cut_from = post.find("</div>")
        # cut_to = post.find("<div style=")
        # news_read = soup(post[cut_from+1:cut_to],"html.parser")
        news_read = soup(post, "html.parser")

        row = {
            "source": str(source),
            "headline": str(headline),
            "address": str(address),
            "author": str(author),
            "date": str(date),
            "image": str(image),
            "news_read": str(news_read)
        }
        today_ng_news.append(row)

    return today_ng_news
