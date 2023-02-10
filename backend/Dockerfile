FROM python:3.9.13
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
VOLUME /code
WORKDIR /code
ADD requirements*.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD /bin/bash
