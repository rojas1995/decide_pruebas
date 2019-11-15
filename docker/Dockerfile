from python:alpine

RUN apk add --no-cache git postgresql-dev gcc libc-dev
RUN apk add --no-cache gcc g++ make libffi-dev python3-dev build-base
RUN apk add --no-cache firefox-esr xvfb

RUN pip install gunicorn
RUN pip install psycopg2
RUN pip install ipdb
RUN pip install ipython

RUN pip install coverage==3.6
RUN pip install selenium 

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
RUN tar -x geckodriver -zf geckodriver-v0.24.0-linux64.tar.gz -O > /usr/bin/geckodriver
RUN chmod +x /usr/bin/geckodriver
RUN rm geckodriver-v0.24.0-linux64.tar.gz

WORKDIR /app

RUN git clone https://github.com/jagalindo/decide.git .
RUN pip install -r requirements.txt

WORKDIR /app/decide

# local settings.py
ADD docker-settings.py /app/decide/local_settings.py

RUN ./manage.py collectstatic

#CMD ["gunicorn", "-w 5", "decide.wsgi", "--timeout=500", "-b 0.0.0.0:5000"]
