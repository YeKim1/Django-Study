FROM python:3
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "study.wsgi:application"]