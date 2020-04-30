FROM python:3.7.3-slim-stretch
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python3","app.py"]