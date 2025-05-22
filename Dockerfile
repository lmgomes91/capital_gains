FROM python:3.11.12-slim-bullseye


WORKDIR /app
COPY . /app/

RUN chmod +x main.py

CMD ["python", "main.py"]
