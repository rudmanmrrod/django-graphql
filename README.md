# Instalar esta aplicación

```mkvirtualenv django-graphql --python=/usr/bin/python3

pip install -r requeriments.txt

python manage.py makemigrations movies
python manage.py migrate

python manage.py runserver
```

# Hacerla paso a paso

```mkvirtualenv django-graphql --python=/usr/bin/python3

pip install django
pip install graphene_django

django-admin startproject DjangoGraphql

cd DjangoGraphql/
pip freeze > requeriments.txt
python manage.py startapp movies

python manage.py makemigrations movies
python manage.py migrate

python manage.py runserver
```
