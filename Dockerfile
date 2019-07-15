FROM python:3.6-alpine

COPY . /online_executor
WORKDIR /online_executor
RUN pip install -r requirements.txt
RUN chmod 644 server.py

CMD ["gunicorn", "-b", "0.0.0.0:8000", "server:app"]
