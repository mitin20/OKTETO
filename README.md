# meme-app by Chat-GPT
#AIAC Create python web app to get Reddit Meme API using flask and give a Dockerfile and K8s manifest


Create python web app with index.html to get and show Reddit Meme API using flask and give a Dockerfile and K8s manifest
ChatGPT
Here is a sample code for the Flask application to retrieve the Reddit Meme API and display it in an HTML template:

Copy
Insert
New
from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/memes')
def get_memes():
    url = 'https://www.reddit.com/r/Memes/new/.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    response = requests.get(url, headers=headers)
    memes = response.json()['data']['children']
    return render_template('index.html', memes=memes)

if __name__ == '__main__':
    app.run(debug=True)
Here is the HTML template (templates/index.html) to display the memes:

Copy
Insert
New
<!DOCTYPE html>
<html>
<head>
    <title>Memes from Reddit</title>
</head>
<body>
    <h1>Memes from Reddit</h1>
    <ul>
        {% for meme in memes %}
        <li>
            <p><a href="{{ meme.data.url }}">{{ meme.data.title }}</a></p>
            <img src="{{ meme.data.url }}" alt="{{ meme.data.title }}">
        </li>
        {% endfor %}
    </ul>
</body>
</html>
And here is the Dockerfile to build an image for the Flask application:

Copy
Insert
New
FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
Finally, here is an example Kubernetes manifest to deploy the Flask application:

Copy
Insert
New
apiVersion: apps/v1
kind: Deployment
metadata:
  name: reddit-memes-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: reddit-memes-app
  template:
    metadata:
      labels:
        app: reddit-memes-app
    spec:
      containers:
        - name: reddit-memes-app
          image: <your_image_name>
          ports:
            - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: reddit-memes-app
spec:
  selector:
    app: reddit-memes-app
  ports:
    - name: http
      port: 5000
      targetPort: 5000
  type: ClusterIP
Note: Don't forget to replace <your_image_name> in the Kubernetes manifest with the actual image name of your Docker image.

get requirements.txt for pip install -r flask and jsonify

Flask==1.1.2
requests==2.25.0

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




