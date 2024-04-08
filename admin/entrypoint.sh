#!/bin/bash

while ! ./manage.py sqlflush > /dev/null 2>&1 ;do
    echo "Waiting for database..."
    sleep 1
done

echo "Collect static files"
./manage.py collectstatic --no-input

echo "Apply database migrations"
./manage.py migrate

echo "Create superuser"
./manage.py createsuperuser --noinput

echo "Compile localized messages"
django-admin compilemessages --ignore=.venv

exec "$@"
