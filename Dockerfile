FROM python:3.11-slim

# Install required system libraries
RUN apt-get update && apt-get install -y libsndfile1 ffmpeg
RUN apt-get install -y git
RUN apt-get install -y build-essential

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN pip install torch
RUN pip install ninja
RUN pip install git+https://github.com/CPJKU/madmom
RUN pip install allin1

RUN pip3 install natten -f https://shi-labs.com/natten/wheels/cpu/torch2.0.0/index.html

RUN pip install --upgrade Flask
RUN pip install --upgrade Werkzeug

COPY . .

EXPOSE 8080
CMD ["python", "main.py"]