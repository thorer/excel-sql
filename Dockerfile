FROM python:3.9-slim-buster

EXPOSE 8080

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY test.py test.py

ENTRYPOINT [ "python3","-u", "test.py"] 
