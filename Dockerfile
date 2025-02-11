FROM python:3.12.6-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m unittest discover

EXPOSE 80

CMD ["uvicorn", "api:app", "--host", "localhost", "--port", "80", "--reload"]
