# 1. Get a lightweight, standard Python computer
FROM python:3.11-slim

# 2. Tell Python not to write annoying hidden cache files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Create a folder inside the Docker computer called /app
WORKDIR /app

# 4. Copy our requirements list into the Docker computer
COPY requirements.txt .

# 5. Tell Docker to install our Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of our code into the Docker computer
COPY . .