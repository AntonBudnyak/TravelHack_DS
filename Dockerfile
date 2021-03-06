FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8080"]
