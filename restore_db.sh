#!/bin/bash

echo "==> Removing all migration files"
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

echo "==> Removing all data from the database..."
python manage.py flush --noinput

echo "==> Migrating to the db"
python manage.py makemigrations
python manage.py migrate

echo "==> Loading user fixtures..."
python manage.py loaddata fixtures/users.json

echo "==> Loading currencys fixtures..."
python manage.py loaddata fixtures/currencys.json

echo "==> Loading employees fixtures..."
python manage.py loaddata fixtures/employees.json

echo "==> Loading soliton users fixtures..."
python manage.py loaddata fixtures/soliton_users.json

echo "==> Done!"
