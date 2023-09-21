FROM python:3.8.3-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PORT=8000

ADD . /app
RUN apk update && apk add python3 \
                        py3-pip \
                        python3-dev \
                        postgresql \ 
                        postgresql-dev \
                        gcc \
                        libc-dev
# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT