Backend app for digital labs booking
====================================

Admin interfaces for managing resources represented as calendars for every
library branch.

Event/calendar models and admin code are heavily inspired by
https://github.com/llazzaro/django-scheduler

Frontend part can be found at -- https://gitlab.com/gorner/tpl-digital-booking


Requirements: Python 3.5 / Django 1.9 / Postgresql / virtualenvwrapper

Installation
~~~~~~~~~~~~~

Configure postgres and set up database digital_hub; see settings.py / DATABASES

.. code-block :: python

    DATABASES = {
         'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'digital_hub',
            'USER': 'alex',
            'PASSWORD': 'alex',
            'HOST': 'localhost',
            'PORT': '5433'
            }
    }


See these instructions on setting up postgres on ubuntu -- https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04


Install django

.. code-block :: bash

    $ mkvirtualenv --python `which python3` digital_hub
    (digital_hub)$ pip install -r requirements.txt


Create, run migrations, create admin user, then start the server in development mode


.. code-block :: bash

    $ workon digital_hub
    (digital_hub) $ cd ${PROJECT_ROOT}/digital_hub
    (digital_hub) $ python manage.py makemigrations
    (digital_hub) $ python manage.py migrate
    (digital_hub) $ python manage.py createsuperuser
    ....

    (digital_hub) $ python manage.py runserver
    System check identified no issues (0 silenced).
    September 18, 2016 - 18:15:29
    Django version 1.9.6, using settings 'digital_hub.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.



Open browser and go to http://127.0.0.1:8000/admin then use username and password
set when running createsuperuser command.