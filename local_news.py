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
