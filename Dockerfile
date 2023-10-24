FROM python:latest

RUN mkdir /opt/wx-app
COPY ./app /opt/wx-app/app
COPY main.py /opt/wx-app/main.py
RUN pip install -r requriements.txt
EXPOSE port
CMD ["python", "/opt/wx-app/main.py"]