from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/')
def get_memes():
    url = 'https://www.reddit.com/r/Memes/new/.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    response = requests.get(url, headers=headers)
    memes = response.json()['data']['children']
    return render_template('index.html', memes=memes)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)


#meme-app-2.0
from flask import Flask, render_template
import request
import json

def get_meme():
#Uncomment these two lines and comment out the other url line if yo
# sr = "/wholesomememes"
# url = "https://meme-api.herokuapp.com/gimme" + sr
url = "https://meme-api.herokuapp.com/gimme"
response = json.loads (requests.request("GET", url).text)
meme_large = response["preview"][-2]
subreddit = response["subreddit"]
return meme_large, subreddit
@app.route("/")
def index():
meme_pic,subreddit = get_meme()
return render_ template("meme_index.html"
meme_pic=meme_pic, subreddit=subreddit)
app.run (host="0.0.0.0", port=80)_
