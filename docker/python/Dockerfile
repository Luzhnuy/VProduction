FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /VProduction
WORKDIR /VProduction
ADD . /VProduction/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install mysqlclient
COPY . /VProduction/

ENTRYPOINT ["./docker/python/entrypoint.sh"]