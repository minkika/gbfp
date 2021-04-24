## Проект "gbfp"
## Командная разработка по методологии Agile:Scrum
## Сайт для поиска работы

### Базовая документация к проекту

Основные системные требования:

* Python 3.9
* Django 3.1
* Зависимости (Python) из requirements.txt

### Установка необходимого ПО
#### обновляем информацию о репозиториях
```
apt update
```
#### Установка virtualenv
```
virtualenv
```
apt install python3-venv
```
#### Настраиваем виртуальное окружение
При необходимости, для установки менеджера пакетов pip выполняем команду:
```
apt install python3-pip
```
Создаем и активируем виртуальное окружение:
```
python3 -m venv /gbfp/venv/gbfp_env
source /gbfp/venv/gbfp_env/bin/activate  
```
Ставим зависимости:
```
pip3 install -r /gbfp/venv/gbfp_env/src/gbfp/requirements.txt
``` 
#### Выполнение миграций и сбор статических файлов проекта
Выполняем миграции:
```
python3 manage.py migrate
```
Собираем статику:
```
python3 manage.py collectstatic
```
#### Заполнить базу данных тестовыми данными (не обязательно)
```
python3 manage.py fill_db
```
#### Тест запуска
```
python3 manage.py runserver
```

### После этого в браузере можно ввести ip-адрес сервера и откроется проект.
