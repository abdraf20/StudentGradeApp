FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# نسخ مجلد src كاملاً
COPY src/ ./src/

CMD ["python", "src/app.py"]