from flask import Flask, json, jsonify, request
from flask_cors import CORS, cross_origin

from local_news import (scrape_fidelinfo, scrape_kwaragist, scrape_kwaralefro,
                        scrape_legit, scrape_todayng)

# from local_news import scrape_legit, scrape_kwaralefro, scrape_todayng, scrape_kwaragist, scrape_theinformant247, scrape_fidelinfo, scrape_freshinsight

app = Flask(__name__)
# cors = CORS(app)
# CORS(app)


@app.route('/')
@cross_origin()
def lost():
    return "Lost? What are you looking for."


@app.route('/api')
@cross_origin()
def apis():
    return "Nothing here for you..."


@app.route('/api/news')
@cross_origin()
def newsIndex():

    data1 = scrape_legit()
    data2 = scrape_kwaralefro()
    data3 = scrape_todayng()
    data4 = scrape_kwaragist()
    data6 = scrape_fidelinfo()

    # removed due to old news
    # data8 = scrape_royalfm()

    data = data1 + data2 + data3 + data4 + data6

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(debug=True, port=9000)
