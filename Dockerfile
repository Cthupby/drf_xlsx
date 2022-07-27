FROM python:3.9

WORKDIR /drf_xlsx

COPY ./requirements.txt /requirements.txt

RUN pip install /requirements.txt

COPY . /drf_xlsx

RUN python manage.py migrate
RUN python manage.py runserver
