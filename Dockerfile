FROM python:3.11.5

COPY . /app

WORKDIR /app

RUN python -m pip install -r requirements/production.txt

EXPOSE 8000

CMD gunicorn -b 0.0.0.0:8000 -w 3 project.wsgi