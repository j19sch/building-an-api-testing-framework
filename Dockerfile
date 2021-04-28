from python:3.6-alpine

EXPOSE 80

RUN pip install gunicorn==20.0.4
RUN pip install falcon==2.0.0

COPY ./api_app/src /src

CMD ["gunicorn", "-b", "0.0.0.0:80", "src.app:app"]
