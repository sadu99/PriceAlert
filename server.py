from flask import Flask, render_template, request
import bloomberg

app = Flask("price_alert")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit")
def submit():
    ticker = request.args.get("ticker")
    start = request.args.get("start")
    end = request.args.get("end")
    data = bloomberg.getIndexData(ticker, start, end)
    return render_template("submit.html", data=data)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
