# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster
WORKDIR /app
RUN pip3.9 install pipenv
COPY . .
RUN pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip3.9 install -r requirements.txt
CMD ["python3", "Bot/__main__.py"]
