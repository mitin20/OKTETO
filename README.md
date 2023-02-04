# meme-app by Chat-GPT
#AIAC Create python web app to get Reddit Meme API using flask and give a Dockerfile and K8s manifest
#Python Web App

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

#index.html
<html>
    <head>
        <title>Random Reddit Meme</title>
    </head>
    <body>
        <h1>Random Reddit Meme</h1>
        <h2>{{memeData.title}}</h2>
        <img src="{{memeData.url}}" />
    </body>
</html>


#Dockerfile
FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

#Kubernetes manifest
apiVersion: v1
kind: Service
metadata:
  name: webapp
  labels:
    app: webapp
spec:
  selector:
    app: webapp
  ports:
  - protocol: TCP
    port: 5000
    targetPort: 5000
  type: LoadBalancer

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp-deployment
spec:
  selector:
    matchLabels:
      app: webapp
  replicas: 3
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        image: webapp-image
        ports:
        - containerPort: 5000
          protocol: TCP
