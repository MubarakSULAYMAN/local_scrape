import requests
from bs4 import BeautifulSoup as soup


def scrape_legit():

    news_url = "https://www.legit.ng/tag/kwara-state-news-today.html"
    source = "Naij.com > Legit.ng"
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all(
        "article", {"class": "c-article-card-no-border"})

    legit_news = []

    for container in containers:
        headline = container.span.getText().strip()
        date = container.div.time.getText().strip()
        image = container.a.picture.img["data-src"]
        address = container.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        # page_soup = soup(read_address.content, "html.parser")
        author = str(page_soup.body.find(
            class_="c-article-info__author").getText().strip())
        post = str(page_soup.body.find(
            class_="l-article__body c-article__body"))

        # cut_from = post.find(">")
        # cut_to = post.find("<div class=")
        # news_read = soup(post[cut_from+1:cut_to],"html.parser")
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
        headline = container.h1.a.getText().strip()
        date = container.div.span.a.time.getText().strip()
        image = container.a.img["src"]
        address = container.div.p.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        author = container.span.span.a.getText().strip()
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
        headline = container.find(
            class_="entry-title td-module-title").getText().strip()
        image = container.div.a.img["src"]
        address = container.div.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        date = str(page_soup.body.find(
            class_="entry-date updated td-module-date").getText().strip())
        author = str(page_soup.body.find(
            class_="td-post-author-name").getText().strip())
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


def scrape_kwaragist():
    news_url = "https://kwaragist.com"
    source = "Kwara Gist"
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("li", {"class": "infinite-post"})

    kwaragist_news = []

    for container in containers:
        headline = container.find(
            class_="mvp-main-blog-text left relative").a.getText().strip()
        image = container.div.a.div.img["src"]
        author = container.find(class_="mvp-blog-author").getText().strip()
        date = container.find(class_="mvp-blog-date").getText().strip()
        address = container.div.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        post = str(page_soup.body.find(
            class_="theiaPostSlider_preloadedSlide"))

        # cut_from = post.find("</div>")
        # cut_to = post.find("<div class=")
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
        kwaragist_news.append(row)

    return kwaragist_news


def scrape_theinformant247():
    news_url = "http://www.theinformant247.com"
    source = "Informant 247"
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("li", {"class": "post-item"})

    theinformant247_news = []

    for container in containers:
        headline = container.find(class_="post-title").a.getText().strip()
        address = container.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        author = str(page_soup.body.find(class_="entry-sub-title"))
        date = str(page_soup.body.find(class_="date meta-item"))
        image = str(page_soup.body.find(class_="entry-content entry clearfix"))
        post = str(page_soup.body.find(class_="entry-content entry clearfix"))

        # cut_from = post.find("</div>")
        # cut_to = post.find("<div class=")
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
        theinformant247_news.append(row)

    return theinformant247_news


def scrape_fidelinfo():
    news_url = "https://www.fidelinfo.com/category/news/"
    source = "Fidel Info"
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("li", {"class": "post-item"})

    fidelinfo_news = []

    for container in containers:
        headline = container.find(class_="post-title").a.getText().strip()
        image = container.a.img["src"]
        date = container.find(class_="date meta-item").getText().strip()
        author = container.find(
            class_="meta-author meta-item").a.getText().strip()
        address = container.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        post = str(page_soup.body.find(class_="entry-content entry clearfix"))

        cut_from = post.find("::before")
        cut_to = post.find("<p>&nbsp;")
        news_read = soup(post[cut_from+1:cut_to], "html.parser")

        row = {
            "source": str(source),
            "headline": str(headline),
            "address": str(address),
            "author": str(author),
            "date": str(date),
            "image": str(image),
            "news_read": str(news_read)
        }
        fidelinfo_news.append(row)

    return fidelinfo_news


# def scrape_freshinsight():
#     news_url = "https://www.freshinsight.tv/"
#     source = "Fresh Insight TV"
#     newsClient = requests.get(news_url)
#     page_html = newsClient.text
#     page_soup = soup(page_html, "html.parser")
#     containers = page_soup.find_all("div", {"class": "featured-inner"})

#     freshinsight_news = []

#     for container in containers:
#         # headline = container.div.h3.a.getText().strip()
#         headline = container.find(class_="rcp-title").getText().strip()
#         image = container.find(class_="rcp-title").a["style"]
#         date = container.find(class_="featured-date").getText().strip()
#         author = container.find(class_="featured-author idel").getText().strip()
#         address = container.div.h3.a["href"]
#         read_address = requests.get(address)
#         page_html = read_address.text
#         page_soup = soup(page_html, "html.parser")
#         post = str(page_soup.body.find(class_="post-body entry-content"))

#         cut_from = post.find("<article>")
#         cut_to = post.find("</article>")
#         news_read = soup(post[cut_from+1:cut_to],"html.parser")

#         row = {
#             "source": str(source),
#             "headline": str(headline),
#             "address": str(address),
#             "author": str(author),
#             "date": str(date),
#             "image": str(image),
#             "news_read": str(news_read)
#         }
#         freshinsight_news.append(row)

#     return freshinsight_news


# def scrape_royalfm():
# news_url = "http://royalfm.net/category/news/local_news/"
# source = "Royal fm - 95.1 MHz"
# newsClient = requests.get(news_url)
# page_html = newsClient.text
# newsClient.close()
# page_soup = soup(page_html, "html.parser")
# containers = page_soup.find_all("div", {"class": "category-local_news"})

# royal_news = []

# for container in containers:
# headline = container.div.a["title"]
# address = container.div.a["href"]
# author = container.find(class_ = "tm_catpost_item_1").getText().strip()
# date = container.find(class_ = "tm_catpost_item_3").getText().strip()
# image = container.find(class_ = "tm_cat_image").a.img["src"]

# fetch_read_address = container.find(class_ = "tmpost-readmore").a["href"]# read_address = requests.get(fetch_read_address)# page_soup = soup(read_address.content, "html.parser")# post = str(page_soup.body.find(class_ = "post"))# cut_from = post.find(">")# cut_to = post.find("<!-- Facebook Comm")# news_read = soup(post[cut_from + 1: cut_to], "html.parser")

# row = {
  # "source": str(source),
  # "headline": str(headline),
  # "address": str(address),
  # "author": str(author),
  # "date": str(date),
  # "image": str(image),
  #"news_read": str(news_read)#
# }
# royal_news.append(row)

# return royal_news
