FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env
RUN echo "=== .env in container ===" && cat .env

COPY app/ ./app/

EXPOSE 5000
CMD ["python", "app/chat_server.py"]
