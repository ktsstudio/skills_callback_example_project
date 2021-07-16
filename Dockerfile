FROM python:3.9.6-alpine3.14
WORKDIR code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT pytest tests/
