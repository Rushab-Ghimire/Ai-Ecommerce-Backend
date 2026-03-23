#!/bin/sh

set -e

echo "Waiting for postgres..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done
echo "PostgreSQL started"

# 1. Move into the 'app' directory where manage.py lives
cd app

# 2. Run the commands
python manage.py migrate

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000