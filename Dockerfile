FROM python:latest
ENV APP_PORT=8888
RUN mkdir /opt/wx-app
COPY ./app /opt/wx-app/app
COPY main.py /opt/wx-app/main.py
RUN pip install -r requriements.txt
EXPOSE ${APP_PORT}
CMD ["python", "/opt/wx-app/main.py"]