#  Галерея API #

Это проект Django REST API, который служит серверной частью для приложения Галерея. API предоставляет конечные точки для создания, извлечения, обновления и удаления сообщений, а также для того, чтобы добавлять и удалять из избраного.
## Getting Started ##

Чтобы начать работу с этим проектом, выполните следующие действия:

1. Клонировать репозиторий:
```
git clone https://github.com/KeenGear/exam_9_dias_daribayev.git
```
Установите зависимости проекта:
```
cd exam_9_dias_daribayev
pip install -r requirements.txt
```
Запустите миграцию базы данных:
```
python manage.py migrate
```
Создайте учетную запись суперпользователя:
```
python manage.py createsuperuser
```
Запустите фикстуры:
```
python manage.py loaddata fixtures/auth.json
python manage.py loaddata fixtures/gallery_app.json
python manage.py loaddata fixtures/users_app.json
```
Запустите сервер:
```
python manage.py runserver
```
Теперь вы должны иметь доступ к API по адресу http://localhost:8000/api/.

## API Endpoints ##

Доступны следующие конечные точки API:

### GET /api/posts/ ###
Возвращает список всех постов.

### POST /api/create-post/ ###
Создает новый пост.

### GET /api/posts/<int:pk>/ ###
Возвращает детали для определенного поста.

### PUT /api/posts/<int:pk>/update/ ###
Обновляет определенный пост.

### DELETE /api/posts/<int:pk>/delete/ ###
Удаляет определенный пост.

### POST /api/like-post/<int:pk>/ ###
Добавить пост в избранное.

### DELETE /api/like-post/<int:pk>/ ###
Удаляет пост из избранного.

## Аутентификация ##

Большинство конечных точек API требуют аутентификации. Для аутентификации включите токен в заголовок Authorization вашего запроса:
```
Authorization: Token <your-token>
```
Чтобы получить токен, отправьте запрос POST на конечную точку api-token-auth с учетными данными вашей учетной записи суперпользователя:
```
{
    "username": "your-username",
    "password": "your-password"
}
```
Ответ будет содержать ваш токен:
```
{
    "token": "<your-token>"
}
```
Для тестирования: 
```
пароль для пользователей: "Bamsters2"
```
