FROM python:alpine
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt 
EXPOSE 4800
ENTRYPOINT ["python", "app.py"]