FROM python:2.7-alpine
WORKDIR "/usr/local/src/cars"
COPY cars.json cars.json
COPY requirements.txt requirements.txt
COPY service.py service.py
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "/usr/local/src/cars/service.py" ]
