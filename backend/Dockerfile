# img
FROM python:3.8-alpine
# django logs in realtime
ENV PYTHONUNBUFFERED=1

# Virtualenv
ENV VIRTUAL_ENV=/backend/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/

# install dependencies
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers postgresql-dev
RUN apk add libpq
RUN pip install -r requirements.txt
RUN apk del .tmp

COPY . /app

EXPOSE 8000

# run the app
# RUN python manage.py migrate
# CMD["python", "manage.py", "runserver", "0.0.0.0:8000"]