Установка и запуск проекта.
Склонируйте репозиторий.

Для запуска приложения необходимо настроить виртуальное окружение 
и установить все необходимые зависимости с помощью команд:
Команда для Windows:
1- python -m venv venv
2- venv\Scripts\activate.bat
3- pip install -r requirements.txt

Создать БД:
1- Выполнить вход sudo -U postgres psql
2- Создать базу данных с помощью следующей команды: CREATE DATABASE bd_name;
3- Выйти \q

Применить миграции:
python manage.py migrate

Для работы с переменными окружениями необходимо заполнить файл .env на основе .env.sample

Для создания суперпользователя 
python manage.py createsuperuser

Для запуска приложения:

python manage.py runserver

Доступ к административной панели: http://127.0.0.1:8000/admin/
