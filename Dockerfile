FROM python:3

WORKDIR /code

COPY ./docs/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD python /code/src/main.py

EXPOSE 8080