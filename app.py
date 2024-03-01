from flask import Flask, redirect,render_template, url_for
from form  import RegistrationForm,LoginForm
import random
app = Flask(__name__)
app.config["SECRET_KEY"]="290964d444b41b98f8c9bd984b71a7c6"
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

@app.route("/register",methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template('register.html',title='register',random=random.random(),form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if(
            form.email.data=="hagar@gmail.com"
            and form.password.data=="Hagar@12"
        ):
            return redirect(url_for("home"))
    return render_template('login.html',title='login',random=random.random(),form=form)

if __name__=="__main__":
    app.run(debug=True)
