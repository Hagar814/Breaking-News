from flask import Flask,render_template

app = Flask(__name__)

news=[
    {"author": "tmohamed@insider.com (Theron Mohamed)",
"title": "'Magnificent 7' tech stocks are dangerously dominant — and recession's still a real risk, top economist warns",
"description": "Deutsche Bank's economics chief Jim Read called out huge tech valuations and said the US economy is now in the \"snipers' alley of recessions.\""},
{"author": "aol.com",
"title": "Nvidia's huge post-earnings stock rally cost short sellers $3 billion",
"description": "None Data from S3 Partners shows $18.3 billion of short interest in Nvidia stock. • None Nvidia is up nearly 70% year to date and hit a milestone market cap of $2 trillion on Thursday. According to data from S3 Partners, investors betting on a decline in Nvid…"},
{"author": "Investing.com",
"title": "Earnings call: Alarm.com reports growth and strategic focus in Q4 2023",
"description": "Earnings call: Alarm.com reports growth and strategic focus in Q4 2023"}
]

@app.route("/")
def home():
    return render_template('home.html',news = news, title='Home')

@app.route("/about")
def about():
    return render_template('about.html',title='About')


if __name__=="__main__":
    app.run(debug=True)