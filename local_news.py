import requests
from bs4
import BeautifulSoup as soup
#import csv
# from csv import writer

def scrape_legit():
    news_url = "https://www.legit.ng/tag/kwara-state-news-today.html"
    source = "Naij.com"
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    # newsClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll(
        "div", {"class": "l-taxonomy-page-hero__list"})

    legit_news = []

    for container in containers:
        x = container.find_all(
            class_="c-article-card-no-border__headline-hover-inner")
        for y in x:
            headline = y.getText().strip()
            # print(headline)
        x = container.find_all(class_="c-article-card-no-border")
        for y in x:
            address = y.a["href"]
            # print(address)
        x = container.find_all(class_='c-article-info__time')
        for y in x:
            date = y.getText().strip()
            # print(date)
        x = container.find_all(class_="c-article-card-no-border")
        for y in x:
            image = y.a.img['src']
            # print(image)
            # news_snip = container.find(class_ = "tmpost-desc").get_text()

        x = container.find_all(class_="c-article-card-no-border")
        for y in x:
            fetch_read_address = y.a["href"]
            # print(fetch_read_address)
            read_address = requests.get(fetch_read_address)
            # print(read_address)

            page_soup = soup(read_address.content, "html.parser")
            # print(page_soup)

            newspage = page_soup.body.find_all(class_="c-article-info")
            x = newspage.find_all(class_='c-article-info__author')
            for y in x:
                author = y.getText().strip()
                # print(author)

            page_soup = soup(read_address.content, "html.parser")
            # print(page_soup)
            x = page_soup.body.find_all(
                class_="l-article__body c-article__body")
            for y in x:
                post = str(y)  # print(post)
                cut_from = post.find('>')
                cut_to = post.find("<div class=")
                news_read = soup(post[cut_from + 1: cut_to], "html.parser")
                print(news_read)

                row = {
                    'source': str(source),
                    'headline': str(headline),
                    'address': str(address),
                    'author': str(author),
                    'date': str(date),
                    'image': str(image),
                    'new_snip': str(news_snip),
                    'news_read': str(news_read)
                }
                legit_news.append(row)

        return legit_news

# def scrape_kwaralefro(): #news_url = "http://www.kwaralefro.com"
#source = "Kwara Legacy Frontier"
#newsClient = requests.get(news_url)# page_html = newsClient.text# page_soup = soup(page_html, "html.parser")
# containers = page_soup.findAll("div", {"class": "container-wrapper"})

# kwaralefro_news = []

#for container in containers: #headline = container.div.p.getText().strip()# address = container.h1.a["href"]
# author = container.find(class_ = "author").getText().strip()
# date = container.find(class_ = "entry-date").getText().strip()
# image = container.find(class_ = "content-excerpt").a.img["src"]

# fetch_read_address = container.find(class_ = "entry").a['href']
# read_address = requests.get(fetch_read_address)# page_soup = soup(read_address.content, "html.parser")
# post = str(page_soup.body.find(class_ = "post"))# cut_from = post.find('>')
# cut_to = post.find('<div class=')
# news_read = soup(post[cut_from + 1: cut_to], "html.parser")

# row = {
  #'source': str(source),
  #'headline': str(headline),
  #'address': str(address),
  #'author': str(author),
  #'date': str(date),
  #'image': str(image),
  #'news_read': str(news_read)
  #}
#kwaralefro_news.append(row)

#return kwaralefro_news

def scrape_todayng():
    news_url = "https://www.today.ng/topic/kwara"
    source = "today.ng"
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("div", {"class": "td-ss-main-content"})

    today_ng_news = []

    for container in containers:
        x = container.find_all(class_="td_module_11")
        for y in x:
            headline = y.getText().strip()
            # print(headline)
        x = container.find_all(class_="item-details")
        for y in x:
            address = y.a["href"]
            # print(address)
        x = container.find_all(class_='td-module-thumb')
        for y in x:
            image = y.a.img['src']
            # print(image)
            # news_snip = container.find(class_ = "tmpost-desc").get_text()
        author = ""
        date = ""

        x = container.find_all(class_="item-details")
        for y in x:
            fetch_read_address = y.a["href"]
            # print(fetch_read_address)
            read_address = requests.get(fetch_read_address)
            # print(read_address)

            page_soup = soup(read_address.content, "html.parser")
            # print(page_soup)

            x = page_soup.body.find_all(class_="td-post-content")
            for y in x:
                post = str(y)
                # print(post)
                cut_from = post.find("/div>")
                cut_to = post.find("<a href=")
                news_read = soup(post[cut_from + 1: cut_to], "html.parser")
                # print(news_read)

                # newspage = page_soup.body.find_all(class_ = "td-container")
                # x = newspage.find_all(class_ = "td-post-author-name")
                # for y in x: #author = y.getText().strip()# print(author)

                # newspage = page_soup.body.find_all(class_ = "td-container")
                # x = fetch_read_address.find(class_ = 'td-post-date')
                # for y in x: #date = y.getText().strip()
                # print(date)

                row = {
                    'source': str(source),
                    'headline': str(headline),
                    'address': str(address),
                    'author': str(author),
                    'date': str(date),
                    'image': str(image),
                    'new_snip': str(news_snip),
                    'news_read': str(news_read)
                }
                today_ng_news.append(row)

    return today_ng_news

def scrape_kwaragist():
    news_url = "https://kwaragist.com"
    source = "Kwara Gist"
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    # newsClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"id": "mvp-home-body"})

    kwaragist_news = []

    for container in containers:
        x = container.find_all(class_="mvp-main-blog-text")
        for y in x:
            headline = y.a.getText().strip()
            # print(headline)
        x = container.find_all(class_="mvp-main-blog-out")
        for y in x:
            address = y.a["href"]
            # print(address)
        x = container.find_all(class_="mvp-blog-author")
        for y in x:
            author = y.getText().strip()
            # print(author)
        x = container.find_all(class_="mvp-blog-date")
        for y in x:
            date = y.getText().strip()
            # print(date)
        x = container.find_all(class_="mvp-main-blog-img")
        for y in x:
            image = y.img['src']
            # print(image)
        # news_snip = container.find(class_ = "tmpost-desc").get_text()
        x = container.find_all(class_="mvp-main-blog-text")
        for y in x:
            fetch_read_address = y.a["href"]
            # print(fetch_read_address)

        read_address = requests.get(fetch_read_address)

        page_soup = soup(read_address.content, "html.parser")
        # print(page_soup)
        x = page_soup.body.find_all(class_="theiaPostSlider_slides")
        for y in x:
            post = str(y)
            print(post)
            cut_from = post.find('<p>&nbsp;</p>')
            cut_to = post.find("<span")
            news_read = soup(post[cut_from + 1: cut_to], "html.parser")

            row = {
                'source': str(source),
                'headline': str(headline),
                'address': str(address),
                'author': str(author),
                'date': str(date),
                'image': str(image),
                'new_snip': str(news_snip),
                'news_read': str(news_read)
            }
            kwaragist_news.append(row)

    return kwaragist_news

# def scrape_theinformant247(): 
#news_url = "http://www.theinformant247.com"
#source = "Informant 247"
#newsClient = requests.get(news_url)
# page_html = newsClient.text
# newsClient.close()# page_soup = soup(page_html, "html.parser")
# containers = page_soup.findAll("div", {"class": "container-wrapper"})

# theinformant247_news = []

#for container in containers: #headline = container.div.a["title"]
# address = container.div.a["href"]
# author = "The Informant247"
#date = container.find(class_ = "time").getText().strip()
# image = container.find(class_ = "attachment-jannah-image-large size-jannah-image-large wp-post-image").a.img['src']
# fetch_read_address = container.find(class_ = "post-details").a["href"]
# read_address = requests.get(fetch_read_address)
# page_soup = soup(read_address.content, "html.parser")
# post = str(page_soup.body.find(class_ = "entry-content"))
# cut_from = post.find('</div>')# cut_to = post.find("<div")
# news_read = soup(post[cut_from + 1: cut_to], "html.parser")

# row = {
  #'source': str(source),
  #'headline': str(headline),
  #'address': str(address),
  #'author': str(author),
  #'date': str(date),
  #'image': str(image),
  #'news_read': str(news_read)#
}
#theinformant247_news.append(row)

#return theinformant247_news

def scrape_fidelinfo():
    news_url = "https://www.fidelinfo.com/category/news/"
    source = "Fidel Info"
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "mag-box-container"})

    fidelinfo_news = []

    for container in containers:
        x = container.find_all_next(class_="post-title")
        for y in x:
            headline = y.getText().strip()  # print(headline)
        x = container.find_all(class_="post-title")
        for y in x:
            address = y.a["href"]  # print(address)
        x = container.find_all(class_="meta-author")
        for y in x:
            author = y.getText().strip()
            # print(author)
        x = container.find_all(class_="date")
        for y in x:
            date = y.getText().strip()  # print(date)
        x = container.find_all(class_="post-thumb")
        for y in x:
            # print(image)# news_snip = container.find(class_ = "post-title").a["href"]
            image = y.img["src"]

        x = container.find_all(class_="post-item")
        for y in x:
            fetch_read_address = y.a["href"]  # print(fetch_address)
        read_address = requests.get(fetch_read_address)  # print(read_address)

        page_soup = soup(read_address.content,
                         "html.parser")  # print(page_soup)
        x = page_soup.body.find_all(class_="post")
        for y in x:
            post = str(y)  # print(post)
            cut_from = post.find("</header>")
            cut_to = post.find("<p>&nbsp;</p>")
            news_read = soup(post[cut_from + 1: cut_to], "html.parser")
            print(news_read)

            row = {
                'source': str(source),
                'headline': str(headline),
                'address': str(address),
                'author': str(author),
                'date': str(date),
                'image': str(image),
                'news_read': str(news_read)
            }
            fidelinfo_news.append(row)

    return fidelinfo_news

# def scrape_royalfm(): 
#news_url = "http://royalfm.net/category/news/local_news/"
#source = "Royal fm - 95.1 MHz"
#newsClient = requests.get(news_url)
# page_html = newsClient.text
# newsClient.close()
# page_soup = soup(page_html, "html.parser")
# containers = page_soup.findAll("div", {"class": "category-local_news"})

# royal_news = []

#for container in containers: 
#headline = container.div.a["title"]
# address = container.div.a["href"]
# author = container.find(class_ = 'tm_catpost_item_1').getText().strip()
# date = container.find(class_ = 'tm_catpost_item_3').getText().strip()
# image = container.find(class_ = 'tm_cat_image').a.img['src']

# fetch_read_address = container.find(class_ = 'tmpost-readmore').a['href']# read_address = requests.get(fetch_read_address)# page_soup = soup(read_address.content, "html.parser")# post = str(page_soup.body.find(class_ = "post"))# cut_from = post.find('>')# cut_to = post.find('<!-- Facebook Comm')# news_read = soup(post[cut_from + 1: cut_to], "html.parser")

# row = {
  #'source': str(source),
  #'headline': str(headline),
  #'address': str(address),
  #'author': str(author),
  #'date': str(date),
  #'image': str(image),
  #'news_read': str(news_read)#
#}
#royal_news.append(row)

#return royal_news
