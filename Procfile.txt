release: python manage.py migrate
web: guicorn mysite.wsgi