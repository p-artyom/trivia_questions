# Сервис получения простых вопросов и ответов

## Описание

Сервис позволяет запрашивать с публичного _API_
[jService](https://jservice.io/) рандомные вопросы. Полученные ответы
сохраняются в базе данных. В случае, если уже имеется такой вопрос в базе
данных, то сервис выполняет дополнительные запросы к публичному _API_ до тех
пор, пока не будет получен уникальный вопрос для викторины. В ответ на запрос
сервис возвращает последний сохранённый вопрос. В случае его отсутствия -
пустой объект.

## Технологии

- Python 3.10.12;
- PostgreSQL 14;
- Django 4.2.5;
- Django REST framework 3.14.0;
- Gunicorn 21.2.0;
- Nginx 1.22.1.

## Запуск приложения локально в docker-контейнерах

Инструкция написана для компьютера с установленной _ОС Windows_ 10 или 11.

- Установите _Windows Subsystem for Linux_ по инструкции с официального сайта
[Microsoft](https://learn.microsoft.com/ru-ru/windows/wsl/install);

- Зайдите на
[официальный сайт Docker](https://www.docker.com/products/docker-desktop/),
скачайте и установите файл _Docker Desktop_;

- В корне проекта создайте .env файл и заполните следующими данными:

  - в переменной `POSTGRES_DB` должно быть название базы данных;

  - в переменной `POSTGRES_USER` должно быть имя пользователя БД;

  - в переменной `POSTGRES_PASSWORD` должен быть пароль пользователя БД;

  - в переменной `DB_HOST` должен быть адрес, по которому _Django_ будет
  соединяться с базой данных;

  - в переменной `DB_PORT` должен быть порт, по которому _Django_ будет
  обращаться к базе данных;

  - в переменную `SECRET_KEY` укажите секретный ключ для конкретной установки
  _Django_;

  - в переменную `DEBUG` укажите значение режима отладки;

  - в переменную `ALLOWED_HOSTS` укажите список строк, представляющих имена
  хоста/домена, которые может обслуживать это _Django_ приложение.

- В терминале в папке с `docker-compose.yml` выполните команду:

```text
docker compose up
```

- Перейдите в новом терминале в директорию, где лежит файл
`docker-compose.yml`, и выполните команды:

```text
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```

- Отправьте POST-запрос на `http://127.0.0.1:8000/api/get_questions/`, передав
в поле `questions_num` количество возвращаемых вопросов от публичного _API_:

```json
{
    "questions_num": 2
}
```

- Сервис вернёт последний сохранённый вопрос, если он присутствует:

```json
{
    "id": 2,
    "id_question": 190681,
    "question": "Just after Botticelli in art dictionaries comes this French Rococo master who also painted goddesses",
    "answer": "Francois Boucher",
    "created_question_at": "2022-12-31T05:32:30.890000+08:00",
    "created": "2023-10-19T19:54:26.749722+08:00",
    "modified": null
}
```

## Автор

Пилипенко Артем
