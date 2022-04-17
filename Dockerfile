FROM python:3.10-slim-buster

WORKDIR /usr/src/app

RUN apt -y update -yqq \
  && apt install -yqq --no-install-recommends build-essential

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uwsgi", "--ini", "uwsgi.ini"]
