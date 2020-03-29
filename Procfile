release: pwd & cd app & python3 manage.py migrate
web: cd app && gunicorn app.wsgi --log-file -
