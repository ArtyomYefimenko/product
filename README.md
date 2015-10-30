# product

1 Installation:

1) $ product

2) $ virtualenv .env

3) $ source .env/bin/activate

4) $ cd app

5) $ pip install -r requirements.txt

6) $ createuser -U postgres product --interactive

7) $ createdb -U product product

8) $ ./manage.py syncdb

9) $ ./manage.py createsuperuser

10) $ ./manage.py collectstatic

11) $ ./manage.py runserver


