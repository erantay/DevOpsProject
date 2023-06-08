FROM python:3-alpine

WORKDIR /app

COPY requirements.txt MainScores.py Scores.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "/app/MainScores.py"]