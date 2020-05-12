#!/bin/bash

echo "==> Removing all data from the database..."
python manage.py flush --noinput

echo "==> Loading user fixtures..."
python manage.py loaddata fixtures/users.json

echo "==> Loading currencys fixtures..."
python manage.py loaddata fixtures/currencys.json

echo "==> Loading employees fixtures..."
python manage.py loaddata fixtures/employees.json

echo "==> Loading soliton users fixtures..."
python manage.py loaddata fixtures/soliton_users.json

echo "==> Done!"
