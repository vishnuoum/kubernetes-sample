FROM python:3.10
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt --progress-bar=off
COPY /code .
EXPOSE 8080
CMD [ "python3", "app.py" ]