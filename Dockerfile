FROM python:3.9.0

WORKDIR /home/

RUN echo "abcded"

RUN git clone https://github.com/dhkangBsn/gis_6ban_3.git

WORKDIR /home/gis_6ban_3/

RUN echo "SECRET_KEY=django-insecure-_4itnwwqc+v1p+f-0-vl1y)x=h@5)qqh8@7hko##0guah@aj(m" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=gis_6ban_3.settings.deploy && python manage.py collectstatic --noinput --settings=gis_6ban_3.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=gis_6ban_3.settings.deploy gis_6ban_3.wsgi --bind 0.0.0.0:8000"]

