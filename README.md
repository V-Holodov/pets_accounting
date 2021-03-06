# Учет питомцев "Pets-Accounting"


![example workflow](https://github.com/v-holodov/pets_accounting/actions/workflows/main.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

## Описание
**Pets-Accounting** - REST API для ведения учета питомцев (собак и кошек). Позволяет добовлять питомцев и фотографии к ним, получать список питомцев и удалять питомцев по списку. Реализована возможность выгрузить список питомцев в json через командную строку

## Технологии
В проекте используются следующие основные пакеты:
- python 3.9
- django 4.0
- djangorestframework 3.12.4
- flake8-isort 4.1.1
- black 21.12b0
- Pillow 8.4.0
- pytz 2021.3
- python-environ 0.4.54
- pytest 6.2.5
- pytest-django 4.5.2
- psycopg2-binary 2.9.2
- gunicorn 20.1.0
- docker 20.10.11


## Пример развернутого проекта

Проект развернут в трех контейнерах 
- *back* - бэкенд-часть,
- *nginx_back* - HTTP-сервер для обработки запросов к бэкенду, отдачи статики django и администрирования django, 
- *db* - база данных postgres.

Проект запущен и доступен по адресу:
[http://51.250.29.41/](http://51.250.29.41/)


## Развертывание  проекта

Обновите систему: 
`sudo apt update && sudo apt upgrade -y`

Установите git и docker:
`sudo apt install git docker.io docker-compose -y`

Склонируйте репозиторий:
`git clone https://github.com/V-Holodov/pets_accounting.git`

Создайте в директории проекта файл .env с переменными окружения для работы с базой данных используя для примера файла .env-example

Команда для развертывания: `sudo docker-compose up` из директории проекта

## Аутентификация
Аутентификация реализована на основе API Key Authentication.

Все запросы должны содержать header X-API-KEY, значение которого должно соответствовать ключу API_KEY в настройках проекта.

## CLI
Реализована возможность выгрузки питомцев из командной строки в stdout в JSON формате.

Команда `sudo docker exec pets_accounting_back_1 python manage.py pets_list`

Команда может принимать на вход необязательный параметр "--has-photos" для выгрузки питомцев только с фото

## Testing
Тестирование в проекте реализована с использованием pytest. 

Выполнение git push в любую из веток запускает проверку кода на соответствие PEP8 и инициирует тесты с помощью функционала Git Actions.

## Коротко о структуре проекта

1. `config` - корневая директория, здесь settings.py джанги
2. `api` - основное приложение проекта
3. `logs` - логи проекта вынесенные из контейнера
4. `.github/workflows` - настройка workflows для gihub actions
6. файлы статики и медиафайлы собраны в одноименных директориях.
7. в директории `nginx` - настройки сервера.
8. `Dockerfile`, `docker-compose.yaml` - развертывания проекта в докер-контенейрах.


## Об авторе
Проект подготовлен [Виталием Холодовым ](https://www.linkedin.com/in/v-holodov/).
