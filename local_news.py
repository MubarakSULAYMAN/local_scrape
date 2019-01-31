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
        headline = container.span.get_text().strip()
        date = container.div.time.get_text().strip()
        image = container.a.picture.img["data-src"]
        address = container.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        author = str(page_soup.body.find(class_="c-article-info__author").get_text().strip())
        post = str(page_soup.body.find(class_="l-article__body c-article__body"))

        weeds = ["READ ALSO:", "NAIJ.com upgrades to Legit.ng: a letter from our Editor-in-Chief Bayo Olupohunda", 
                 "PAY ATTENTION:", "Download our mobile app to enjoy the latest news updates", "PAY ATTENTION: ", 
                 "Access your favourite news site Legit.ng instantly in 3 simple steps", "Disclaimer: ", 
                 "The views and opinions expressed here are those of the author and do not necessarily reflect the official policy or position of", 
                 "Your own opinion articles are welcome at info@corp.legit.ng— drop an email telling us what you want to write about and why. More details in ",
                 "Legit.ng’s step-by-step guide for guest contributors. ", "We’re ready to trade your news for our money: submit news and photo reports from your area using our Citizen Journalism App. ",
                 "Contact us if you have any feedback, suggestions, complaints or compliments. We are also available on ", "Twitter.", "Legit.tv", 
                 "Install our latest app for Android, read best news on Nigeria’s", "#1 news app"]
        for weed in weeds:
            post = post.replace(weed, "")

        # x = d4.find('<div class="embed-container"')
        start = post.find('<a href="https://www.youtube.com')
        end = start+post[start+10:].find('</a>')
        start, end
        final = post[0:start-197]

        news_read = soup(final, "html.parser")
          
        row = {
            "source": str(source),
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
    containers = page_soup.find_all("article", {"class": "content-excerpt"})

    kwaralefro_news = []

    for container in containers:
        headline = container.h1.a.get_text().strip()
        # image = page_soup.a.img["src"]
        date = container.div.span.a.time.get_text().strip()
        address = container.div.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        author = container.find(class_="meta-author").get_text().strip()
        post = str(page_soup.body.find(class_="entry clearfix"))

        start = post.find('<div class=\"sharedaddy')
        end = start+post[start+10:].find("<div class=\"sharedaddy")
        start, end
        final = post[0:start-5]

        news_read = soup(final, "html.parser")

        row = {
        "source": str(source),
        "headline": str(headline),
        "address": str(address),
        "author": str(author),
        "date": str(date),
        # "image": str(image),
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

        start = post.find("Get more stories like this on")
        end = start+post[start+10:].find("></div></div>")
        start, end
        final = post[0:start-60]

        news_read = soup(final, "html.parser")

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
        headline = container.find(class_="mvp-main-blog-text left relative").a.get_text().strip()
        image = container.div.a.div.img["src"]
        author = container.find(class_="mvp-blog-author").get_text().strip()
        date = container.find(class_="mvp-blog-date").get_text().strip()
        address = container.div.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        post = str(page_soup.body.find(class_="theiaPostSlider_preloadedSlide"))

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
        headline = container.find(class_="post-title").a.get_text().strip()
        address = container.a['href']
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        author = str(page_soup.body.find(class_="entry-sub-title"))
        date = str(page_soup.body.find(class_="date meta-item"))
        image = str(page_soup.body.find(class_="entry-content entry clearfix"))
        post = str(page_soup.body.find(class_="entry-content entry clearfix"))

        start = post.find('<div class="heateorFfcClear"></div>')
        end = start+post[start+10:].find("</span></div></div>")
        start, end
        final = post[0:start-7]

        news_read = soup(final, "html.parser")

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
        headline = container.find(class_="post-title").a.get_text().strip()
        image = container.a.img["src"]
        date = container.find(class_="date meta-item").get_text().strip()
        author = container.find(class_="meta-author meta-item").a.get_text().strip()
        address = container.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        post = str(page_soup.body.find(class_="entry-content entry clearfix"))

        cut_from = post.find("::before")
        cut_to = post.find("<p>&nbsp;")
        news_read = soup(post[cut_from+1:cut_to],"html.parser")

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


def scrape_freshinsight():
    news_url = "https://www.freshinsight.tv/"
    source = "Fresh Insight TV"
    newsClient = requests.get(news_url)
    page_html = newsClient.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("div", {"class": "post-outer"})

    freshinsight_news = []

    for container in containers:
        date = container.find(class_="dtreviewed").get_text().strip()
        address = container.div.div.div.a["href"]
        read_address = requests.get(address)
        page_html = read_address.text
        page_soup = soup(page_html, "html.parser")
        headline = page_soup.find(class_="post-head").get_text().strip()
        image = page_soup.find(class_="separator").a.img["src"]
        author_area = page_soup.find(class_="post-body entry-content").get_text().strip()
        author1 = author_area.find("By")
        author2 = author_area.find("\n")
        author = soup(author_area[author1+3:author2],"html.parser")

        post = str(page_soup.body.find(class_="post-body entry-content"))

        cut_from = post.find("<article>")
        cut_to = post.find("</article>")
        news_read = soup(post[cut_from+1:cut_to],"html.parser")

        row = {
            "source": str(source),
            "headline": str(headline),
            "address": str(address),
            "author": str(author),
            "date": str(date),
            "image": str(image),
            "news_read": str(news_read)
        }
        freshinsight_news.append(row)

    return freshinsight_news


# def scrape_guardian():

#     news_url = "https://guardian.ng/tag/kwara-state/"
#     source = "TheGuardian News" 
#     newsClient = requests.get(news_url)
#     page_html = newsClient.text
#     page_soup = soup(page_html, "html.parser")
#     containers = page_soup.find_all("div", {"class" : "row"})

#     guardian_news = []

#     for container in containers:
        # headline = container.find(class_="headline").get_text()
        # date = container.find(class_="age").get_text().strip()
        # image = container.find(class_="title").a.img["src"]
        # address = container.div.a
        # print(address)
        # read_address = requests.get(address)
        # page_html = read_address.text
        # page_soup = soup(page_html, "html.parser")
        # author = str(page_soup.body.find(class_="single-article-author").get_text().strip())
        # post = str(page_soup.body.find(class_="article"))

        # news_read = soup(post, "html.parser")
          
        # row = {
        #     "source": str(source),
            # "headline": str(headline),
            # "address": str(address),
            # "date": str(date),
            # "image": str(image),
            # "author": str(author),
    #         "news_read": str(news_read)
    #         }
    #     guardian_news.append(row)
                
    # return guardian_news


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
# author = container.find(class_ = "tm_catpost_item_1").get_text().strip()
# date = container.find(class_ = "tm_catpost_item_3").get_text().strip()
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
