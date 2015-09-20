from flask import Flask, render_template, request, jsonify
from encoders import DecimalEncoder
import bloomberg
import json
from twilio.rest import TwilioRestClient 

app = Flask("price_alert")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit")
def submit():
    ticker = request.args.get("ticker")
    start = request.args.get("start")
    end = request.args.get("end")
    endPrice = request.args.get("endPrice")
    model_data = bloomberg.getIndexData(ticker, start, end)
    return render_template("submit.html", data=model_data, endPrice=endPrice);

@app.route("/tickers")
def getTickers():
	tickers = bloomberg.getTickers()
	return json.dumps(tickers, cls=DecimalEncoder)

@app.route("/twilio")
def sendMessage():
	ACCOUNT_SID = "ACdc7d2a4a98d67f7782feb96c317666e7" 
	AUTH_TOKEN = "8f7e2fb53338185baa8309ee1fb8cadc" 
	 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	 
	client.messages.create(
		to="+16476099168", 
		from_="+15817004128", 
		body="You need to buy index NOWWWW",  
	)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
