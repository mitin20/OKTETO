# meme-app by Chat-GPT
#AIAC Create python web app to get Reddit Meme API using flask and give a Dockerfile and K8s manifest


Create python web app with styled index.html to get and show Reddit Meme API using flask and give a Dockerfile and K8s manifest
ChatGPT
Here's a basic template for the web app using flask and bootstrap for styling:

Copy
Insert
New
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
    app.run(debug=True)
Here's a simple index.html file using bootstrap:

Copy
Insert
New
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <title>Reddit Memes</title>
</head>
<body>
  <div class="container">
    <h1>Reddit Memes</h1>
    {% for meme in memes %}
    <div class="row">
      <div class="col-md-4">
        <img src="{{ meme.data.thumbnail }}" alt="Meme thumbnail">
      </div>
      <div class="col-md-8">
        <h2>{{ meme.data.title }}</h2>
        <p>{{ meme.data.selftext }}</p>
      </div>
    </div>
    {% endfor %}
  </div>
</body>
</html>
Here's a Dockerfile that packages the app as a Docker image:

Copy
Insert
New
FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
And here's a simple k8s-manifest.yml to deploy this app on a Kubernetes cluster:

Copy
Insert
New
apiVersion: apps/v1
kind: Deployment
metadata:
  name: reddit-memes
spec:
  replicas: 1
  selector:
    matchLabels:
      app: reddit-memes
  template:
    metadata:
      labels:
        app: reddit-memes
    spec:
      containers:
      - name: reddit-memes
        image: <your-docker-image>
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: reddit-memes
spec:
  selector:
    app: reddit-memes
  ports:
  - name: http
    port: 5000
    targetPort: 5000
  type: ClusterIP
This is just a basic example to get you started. You can customize it further based on your needs.

get requirements.txt for pip install -r flask and jsonify

# Requirements.txt
Flask>=1.1.2
requests
jsonify

######################## For Locall ######################################
how to run above python app locally

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
. venv/bin/activate

Install the required packages:
pip install -r requirements.txt

Run the app:
python app.py

Visit http://localhost:5000/memes

fix mac error No module named venv using brew
brew install python3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
Visit http://localhost:5000/memes

get requirements.txt for pip install requests
requests




