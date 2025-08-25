#!/usr/bin/env bash
# Exit on error
set -o errexit

# Initial setup
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
python manage.py migrate
python wizard.py

# mkdir -p staticfiles
python manage.py collectstatic
