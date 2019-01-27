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

        t = re.search("<a>", "</a>")
        u = post.strip(t)

        news_read = soup(u, "html.parser")
        
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
