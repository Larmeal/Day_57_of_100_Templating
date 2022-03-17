from flask import Flask, render_template
import requests

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
content = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", contents=content)

@app.route('/post/<int:id>')
def get_posts(id):
    post_number = content[id]
    return render_template("post.html", id_post=post_number)


if __name__ == "__main__":
    app.run(debug=True)
