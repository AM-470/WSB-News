from flask import Flask, render_template
from fetch_posts import get_news_posts

app = Flask(__name__)

@app.route('/')
def index():
    posts = get_news_posts()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
