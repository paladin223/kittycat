# Кошачья помощь

[![Python Linting](https://github.com/paladin223/kittycat/actions/workflows/python-package.yml/badge.svg)](https://github.com/paladin223/kittycat/actions/workflows/python-package.yml)

# быстре команды - быстрые решения

python ./cathelp/manage.py makemigrations
python ./cathelp/manage.py migrate --run-syncdb
python ./cathelp/manage.py loaddata "data.json"

| задача | code |
| :---: | :--- |
| # Создание фикстуры | `python -Xutf8 ./cathelp/manage.py dumpdata -e contenttypes -e auth.Permission -e thumbnail.kvstore -e sessions.session --indent 2 -o data.json`|
| # Подгрузка фикстуры | `python ./cathelp/manage.py makemigrations`</br> `python ./cathelp/manage.py migrate --run-syncdb` </br> `python ./cathelp/manage.py loaddata "data.json"`|
| # Очистка media/cache | `python manage.py thumbnail cleanup` |