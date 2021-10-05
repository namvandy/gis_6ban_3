FROM python:3.9.7

WORKDIR /home/

RUN echo "gogoing"

RUN git clone https://github.com/dhkangBsn/gis_6ban_3.git

WORKDIR /home/gis_6ban_3/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=gis_6ban_3.settings.deploy && python manage.py collectstatic --noinput --settings=gis_6ban_3.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=gis_6ban_3.settings.deploy gis_6ban_3.wsgi --bind 0.0.0.0:8000"]

