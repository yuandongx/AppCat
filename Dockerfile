FROM python:latest
ENV APP_PORT=8888
RUN mkdir /opt/wx-app
COPY ./app /opt/wx-app/app
COPY main.py /opt/wx-app/main.py
COPY  requirements.txt /opt/wx-app/requirements.txt
RUN pip install -r requirements.txt
EXPOSE ${APP_PORT}
CMD ["python", "/opt/wx-app/main.py"]