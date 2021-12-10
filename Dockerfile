FROM python:3.10.1-alpine3.15

RUN pip install requests
RUN mkdir /app
WORKDIR /app
COPY ./main.py /app/main.py
CMD ["python", "/app/main.py"]
