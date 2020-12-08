FROM python:latest
RUN pip install requests twilio
WORKDIR /src
RUN pip install flask
RUN pip install pandas
RUN pip install google-cloud-vision