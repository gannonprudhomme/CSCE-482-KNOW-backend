FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY . /app
RUN pip install pipenv
RUN pipenv install -d

COPY docker-entrypoint.sh /usr/local/bin
# Needed for GitHub Actions
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
