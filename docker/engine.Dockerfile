FROM python:3.11-slim

WORKDIR /app
COPY engine/ .

RUN pip install -r requirements.txt
CMD ["python", "main.py"]