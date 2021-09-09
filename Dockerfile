FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/dhkangBsn/gis_6ban_3.git

WORKDIR /home/dhkang/

RUN echo "SECRET_KEY=django-insecure-_4itnwwqc+v1p+f-0-vl1y)x=h@5)qqh8@7hko##0guah@aj(m" > .env

RUN pip install gunicorn

RUN pip install -r requirements.txt

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "gis_6ban_3.wsgi", "--bind", "0.0.0.0:8000"]

    