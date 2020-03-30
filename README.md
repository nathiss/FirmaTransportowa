# Firma Transportowa

## Install
```sh
 $ virtualenv -p python3 env
 $ source env/bin/activate
 (env) $ pip3 install -r requirements-dev.txt
```

## Run server
```sh
 (env) $ cd app
 (env) $ ./manage.py makemigrations  # only once after cloning the repo
 (env) $ ./manage.py migrate         # only once before the first run
 (env) $ ./manage.py runserver 0.0.0.0:8080
```

## Create a superuser account
```sh
 (env) $ ./manage.py createsuperuser  # an interactive method
```
