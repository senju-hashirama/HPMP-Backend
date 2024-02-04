FROM python:3.12.1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir fastapi[all]

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/app

