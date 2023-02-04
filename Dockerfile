#FROM python:3.7 

#COPY . /app

#WORKDIR /app

#RUN pip3 install -r requirements.txt

#ENTRYPOINT ["python3"]

#CMD ["app.py"]

#######################################

FROM python:3

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV FLASK_APP app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
