FROM docker.io/python:3.12

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

# Pipfile contains requests
COPY Pipfile.lock /usr/src/
COPY Pipfile /usr/src/
COPY avantia.py /usr/src/
COPY app/ /usr/src/app/

WORKDIR /usr/src

RUN pip install pipenv

RUN pipenv sync

ENV FLASK_APP=avantia.py

CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]