FROM python:3.5-alpine
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
CMD ["python", "app.py"]