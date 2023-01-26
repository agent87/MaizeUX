FROM python:3.10.7

WORKDIR home

COPY . .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN gdown https://drive.google.com/u/0/uc?id=1egGjBDWpd_i5Ny_WhPYm_hiU03pvCh8S 

RUN mkdir temp

CMD streamlit run app.py --server.port 80
