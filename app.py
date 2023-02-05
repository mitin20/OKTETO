from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://www.reddit.com/r/memes/new/.json"
    res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    memes = res.json()["data"]["children"]
    return render_template('index.html', memes=memes)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
