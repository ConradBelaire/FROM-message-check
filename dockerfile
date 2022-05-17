FROM python:latest
WORKDIR /code
COPY ./code /code/
CMD [ "python", "main.py" ]
