FROM python:3.6

RUN adduser --disabled-password codebreaker-cv

WORKDIR /home/codebreaker-cv

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY bin bin
COPY codebreaker_cv.py boot.sh ./
RUN chmod +x boot.sh

RUN chown -R codebreaker-cv:codebreaker-cv ./
USER codebreaker-cv

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]