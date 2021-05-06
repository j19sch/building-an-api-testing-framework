from python:3.6-alpine

EXPOSE 80

RUN pip install gunicorn==20.0.4
RUN pip install falcon==3.0.0

COPY ./api_app/src /api_app/src

CMD ["gunicorn", "-b", "0.0.0.0:80", "api_app.src.app"]
