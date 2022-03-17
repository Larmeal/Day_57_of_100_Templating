from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    time_now = dt.datetime.now().strftime("%Y")
    return render_template("index.html", num=time_now)

@app.route("/guess/<name>")
def guess(name):
    document = {
    "name": name
    }

    response_age = requests.get("https://api.agify.io", params=document)
    response_age.raise_for_status()
    age = response_age.json()

    response_gender = requests.get("https://api.genderize.io", params=document)
    response_gender.raise_for_status()
    gender = response_gender.json()

    return render_template("guess.html",  age=age["age"], gen=gender["gender"], name=age["name"])

@app.route("/blog")
def blog_posts():
    response_age = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response_age.raise_for_status()
    blog_all = response_age.json()

    return render_template("blog.html", posts=blog_all)





if __name__ == "__main__":
    app.run(debug=True)