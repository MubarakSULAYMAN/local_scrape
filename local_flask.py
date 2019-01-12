from flask import Flask, json, jsonify, request

import local_news

from local_news import scrape_legit, scrape_kwaralefro, scrape_todayng, scrape_kwaragist, scrape_theinformant247,  scrape_fidelinfo, scrape_royalfm

app = Flask(__name__)

@app.route('/')
def  lost():
    return "Lost? What are you looking for."

@app.route('/api')
def  apis():
    return "Nothing here for you..."

@app.route('/api/news')
def newsIndex():

    data1 = scrape_legit()
    # data2 = scrape_kwaralefro()
    data3 = scrape_todayng()
    data4= scrape_kwaragist()
    # data5 = scrape_theinformant247()
    data6 = scrape_fidelinfo()

    # removed due to old news
    # data7 = scrape_royalfm()
    
    # data = data1 + data2 + data3 + data4 + data5 + data6 + data7

    data = data1 + data3 + data4 + data6 

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(debug = True, port = 9000)