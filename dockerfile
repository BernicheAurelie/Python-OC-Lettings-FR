FROM python:3.8.3-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PORT=8000

ADD . /app
RUN apk update && apk add python3-dev \
                        gcc \
                        postgresql \ 
                        postgresql-dev \
                        libc-dev
# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
# pip install --no-binary :all: psutil &&
RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput

RUN ls /app/staticfiles && ls /app/staticfiles/admin

EXPOSE 8000

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT