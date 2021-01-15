FROM python:latest
RUN pip install requests twilio
WORKDIR /src
RUN pip install flask
RUN pip install pandas
RUN pip install google-cloud-vision
RUN pip install google-cloud-translate==2.0.0
RUN pip install txtai
RUN pip install google-search-results