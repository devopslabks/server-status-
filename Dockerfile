FROM python:3.12-slim

WORKDIR /app

COPY server_status.py .

CMD ["python3", "server_status.py"]



