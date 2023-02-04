from flask import Flask, render_template
import requests
 
app = Flask(__name__)

# Home/Index route
@app.route('/')
def index():
    response = requests.get("https://www.reddit.com/r/meme/top/.json?limit=1")
    memeData = response.json()['data']['children'][0]['data']
    return render_template('index.html', memeData=memeData)
 
if __name__ == '__main__':
    app.run(debug=True)
