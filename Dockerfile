FROM python:3.9-slim-buster

EXPOSE 8080

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "/test.py"] 
