REM py manage.py makemigrations
REM py manage.py migrate
py manage.py clear_and_migrate
py manage.py fill_db
py manage.py runserver