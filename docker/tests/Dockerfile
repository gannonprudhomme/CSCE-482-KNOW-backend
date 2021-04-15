# Identical copy to the one in the root of the project
FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY . /app
RUN pip install pipenv
RUN pipenv install -d

COPY docker/tests/tests-entrypoint.sh /usr/local/bin
RUN chmod 755 /usr/local/bin/tests-entrypoint.sh
ENTRYPOINT ["tests-entrypoint.sh"]
