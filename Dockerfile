FROM python:latest as app

WORKDIR /code
COPY . .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

ENTRYPOINT ["python3", "main.py"]