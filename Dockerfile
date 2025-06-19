FROM python:3.13-alpine

RUN apk add --no-cache libheif-tools libjpeg-turbo

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py .

CMD ["python", "bot.py"]
