python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python manage.py migrate && export DJANGO_SUPERUSER_PASSWORD=admin && python manage.py createsuperuser --noinput --username admin --email admin@example.org && python manage.py create_blog_posts
