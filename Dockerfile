FROM python:3.7
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
RUN pip install yandex-music
CMD ["python", "bot.py"]