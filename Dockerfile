FROM python:3.8

WORKDIR /app

RUN mkdir -p model_files
RUN mkdir -p data

ADD data/test_photo.jpeg data/test_photo.jpeg
ADD model_files/50.pth model_files/50.pth
ADD run.py run.py
ADD requirements.txt requirements.txt
ADD model_files/model.py model.py
ADD utils/utils.py utils.py
ADD utils/send_data.py send_data.py

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "run:app" ]