source .venv/bin/activate
pip freeze > requirements.txt 
pip install -r requirements.txt
django-admin startproject product-catalog
python manage.py startapp app
python manage.py runserver 