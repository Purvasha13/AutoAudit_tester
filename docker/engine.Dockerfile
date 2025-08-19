FROM python:3.11-slim

WORKDIR /app

COPY . /app

# Install dependencies if needed (none for now)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]

COPY engine/ .

RUN pip install -r requirements.txt
CMD ["python", "main.py"]

