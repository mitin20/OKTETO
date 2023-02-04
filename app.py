import json
import flask
from flask import Flask 

app = Flask(__name__)

@app.route('/memes/api')
def get_memes():
    url = "https://www.reddit.com/r/memes/top.json?t=week"
    response = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    if response.status_code == 200:
        data = response.json()
        memes = []

        for item in data['data']['children']:
            meme = item['data']
            memes.append(meme)

        return json.dumps(memes)

if __name__ == '__main__':
    app.run()
