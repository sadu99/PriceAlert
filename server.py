from flask import Flask, render_template, request, jsonify
from encoders import DecimalEncoder
import bloomberg
import json

app = Flask("price_alert")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit")
def submit():
    ticker = request.args.get("ticker")
    start = request.args.get("start")
    end = request.args.get("end")
    model_data = bloomberg.getIndexData(ticker, start, end)
    return render_template("submit.html", data=model_data)

@app.route("/tickers")
def getTickers():
	tickers = bloomberg.getTickers()
	return json.dumps(tickers, cls=DecimalEncoder)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
