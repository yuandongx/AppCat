FROM python:3.12-alpine3.18
ENV APP_PORT=8888
RUN mkdir /opt/wx-app
COPY ./app /opt/wx-app/app
COPY main.py /opt/wx-app/main.py
COPY  requirements.txt /opt/wx-app/requirements.txt
RUN pip install --upgrade pip && pip install -r /opt/wx-app/requirements.txt
EXPOSE ${APP_PORT}
CMD ["python", "/opt/wx-app/main.py"]
