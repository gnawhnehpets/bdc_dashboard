#!/usr/bin/bash

# Activate virtual environment
source /opt/venv/bin/activate

# Apply database migrations
echo "Apply database migrations"
python3 manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

# Create super user
python3 create_superuser.py

# Start server
echo "Starting server"
python3 manage.py runserver 0.0.0.0:8000
