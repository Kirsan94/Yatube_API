# api_final
Домашняя работа в рамках курса Python-разработчик от "Яндекс.Практикум".
Курс API: интерфейс взаимодействия программ

В рамках данной работы был написан API для форума-дневника Yatube, созданного в предыдущих спринтах.
Данноый API позволяет:
  Создавать и редактировать посты;
  Добавлять посты в группы;
  Оставлять комментарии;
  Подписываться на любимых авторов;
  API поддерживает авторизацию и ограничения доступа.


Чтобы развернуть проект на локальной машине необходимо:
  Установить и запустить локальное окружение
    pytnon -m venv venv
    . venv/Scripts/activate
  Установить зависимости
    pip install -r requirements.txt
  Перейти в папку, где лежит manage.py и сделать миграции
    python manage.py migrate
  Запустить сервер
    python manage.py runserver


Примеры запросов к API:

  GET http://127.0.0.1:8000/api/v1/posts/
    [
        {
            "id": 1,
            "author": "admin",
            "group": 1,
            "text": "All Hail Luna!",
            "pub_date": "2022-04-16T10:24:08.266453Z",
            "image": "http://127.0.0.1:8000/api/v1/posts/posts/Luna.jpg"
        },
        {
            "id": 2,
            "author": "lirsan",
            "group": 2,
           "text": "Hail Luna Indeed!",
            "pub_date": "2022-04-16T10:24:25.425257Z",
            "image": "http://127.0.0.1:8000/api/v1/posts/posts/Luna_Eyes.jpg"
        },
        {
            "id": 3,
            "author": "lirsan",
            "group": 2,
            "text": "terst string",
            "pub_date": "2022-04-16T13:33:58.154349Z",
            "image": null
        }
    ]
    
  GET http://127.0.0.1:8000/api/v1/posts/1/comments/
    {
        "id": 3,
        "author": "lirsan",
        "post": 1,
        "text": "Greetings, first brother!\r\nI will carry her blessing to the next world.",
        "created": "2022-04-16T10:47:30.953719Z"
    }
    
  GET http://127.0.0.1:8000/api/v1/follow/
    [
       {
           "user": "lirsan",
           "following": "admin"
       }
    ]
    
  GET http://127.0.0.1:8000/api/v1/groups/
    [
        {
            "id": 1,
            "title": "Origin",
            "slug": "origin",
            "description": "Group for origin post"
        },
        {
            "id": 2,
            "title": "New",
            "slug": "new",
            "description": "Group for new posts"
        }
    ]
