# Stage 1: Build Stage
FROM python:3.8-slim AS Build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

COPY . .

RUN pip install --prefix=/install flask mysqlclient

# Stage 2: Production Stage
FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libmariadb3 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=Build /install /usr/local
COPY --from=Build /app /app

EXPOSE 5000

CMD ["python", "app.py"]