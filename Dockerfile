FROM python:3.8

WORKDIR /parser

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=manage.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
