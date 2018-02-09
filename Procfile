web: python my_django_app/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT minimundo/settings.py 
web: gunicorn minimundo.wsgi --log-file -