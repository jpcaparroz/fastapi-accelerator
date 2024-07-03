FROM python:3

WORKDIR /code

COPY ./docs/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/app

CMD ["python", ".\code\app\src\main.py"]