# Stacja Benzynowa

## Install
```sh
 $ virtualenv env
 $ source env/bin/activate
 $ pip3 install -r requirements.txt
```

## Run server
```sh
 $ cd app
 $ ./manage.py makemigrations  # only once after cloning the repo
 $ ./manage.py migrate         # only once before the first run
 $ ./manage.py runserver 0.0.0.0:8080
```
