#!/usr/bin/env python./manage.py startapp products      
"""Django's command-line utility for administrative tasks."""
import os
import sys

# разворачивание проекта 
# python3 -m venv venv   для создания виртуального окружения  или  start python -m venv venv
# для активации окружения :venv\Scripts\activate(venv)
# для установки джанго  pip install Django==3.2.13
# django-admin startproject nameproject для вызова создания этой папки со всеми всттроенными файлами
# python manage.py startapp main  для создания нового приложения(файла,страницы) после создания не забудь добавить фаил в "installed_app" в "setting.py" (зарегестрировать)


# ./manage.py startapp products      - для создания приложения
# python manage.py migrate 

# python manage.py shell




def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstpr.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

    # python manage.py runserver
