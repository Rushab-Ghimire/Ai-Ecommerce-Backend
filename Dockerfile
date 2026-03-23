FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 1. Copy everything into /app
COPY . .

# 2. Fix the path: it's inside 'scripts' relative to our current /app folder
RUN chmod +x ./scripts/run.sh

# 3. Update the PATH so it finds our script
ENV PATH="/app/scripts:$PATH"

CMD ["run.sh"]