FROM python:3.9-slim
EXPOSE 8080
RUN apt-get update
RUN apt-get install -y gcc
WORKDIR /app
ENV PATH="{$PATH}:/root/.local/bin"
COPY requirements.txt /app/
RUN CFLAGS="-fcommon" pip install rpi.gpio
RUN pip install -r requirements.txt

COPY . .
CMD gunicorn -b 0.0.0.0:8080 wsgi:app
