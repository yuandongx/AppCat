FROM python:3.12-alpine3.18

ARG  WORK_SPACE=/opt/wx-app

ENV APP_PORT=8000

ENV APP_MONGODB_URL=mongodb://root:admin$12345@mongo:27017/

ENV APP_WEB_PORT=80

ENV APP_LOG_FILE=$WORK_SPACE/log/app.log

ENV APP_WORK_SPACE=$WORK_SPACE

COPY ./app /opt/wx-app/app

COPY ./app.sh /usr/local/bin/app

COPY main.py $WORK_SPACE/main.py

COPY requirements.txt  $WORK_SPACE/requirements.txt

RUN mkdir -p $WORK_SPACE/log && \
    chmod 511 /usr/local/bin/app &&\
    pip install --upgrade pip && pip install -r $WORK_SPACE/requirements.txt

EXPOSE $WEB_PORT

CMD [ "tail", "-f", "/dev/null" ]
