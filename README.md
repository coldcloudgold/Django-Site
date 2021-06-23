# Site


## Суть проекта:

Социальная сеть, с модерацией записей администраторами.


## Стек:

1. База данных: **PostgreSQL**.

2. Фреймворк: **Django**.

3. Очередь (задача с периодическим выполнением): **Celery**.

4. Брокер сообщений: **RabbitMQ**.

5. Кэшироование: **Memcached**.

6. WSGI: **Gunicorn**.

7. Веб-сервер: **Nginx**.

8. Развертывание: **Docker-Compose**. 


## Пример работы:

### Регистрация:

#### Через социльные сети:

![alt](https://github.com/coldcloudgold/illustration/blob/main/Project/Site/Social%20GitHub.gif)

#### Обычная регистрация:

![alt](https://github.com/coldcloudgold/illustration/blob/main/Project/Site/Default%20reg.gif)

## Добавление записи:

![alt](https://github.com/coldcloudgold/illustration/blob/main/Project/Site/Add_post.gif)

### Оповещение администратора, проверка и добавление записи  в общую ленту:

![alt](https://github.com/coldcloudgold/illustration/blob/main/Project/Site/Check_admin_post.gif)

### Система подписок на интересных авторов, комментарии, RSS-лента:

![alt](https://github.com/coldcloudgold/illustration/blob/main/Project/Site/Sub_comment_RSS.gif)

## Запуск проекта:

### Dev:

1. Изменить название *example.env* на *.env*, заранее внеся в него коррективы.

2. Запустить проект:

`mkdir media/ static/ dev_send_mail/ ; ./dev_entrypoint.sh`

3. Перейти в браузере по адресу:

`127.0.0.1:8080`

### Prod:

1. Изменить название *example.env* на *.env*, заранее внеся в него коррективы.

2. Убедиться, что необходимые порты для работы проекта не заняты (8080 - nginx, 5433 - postgres, 5673 - rabbitmq, 8001 - django/gunicorn, 11212 - memcached):

`sudo netstat -tulpn | grep :<xxxx>`

где `xxxx` - номер порта.

3. Если на данных портах запущены стандартные сервисы, их необходимо выключить:

```
sudo kill `sudo lsof -t -i:<xxxx>`
```

4. Создать docker-compose:

`mkdir media/ static/ ; docker-compose build`

5. Запустить docker-compose:

`docker-compose up -d`

Примерно через 30 секунд сервис станет пригодным для использования.

6. Перейти в браузере по адресу:

`127.0.0.1:8080`

7. Остановить и удалить docker-compose:

`docker-compose down -v`

## Полезное:

### Зайти в панель администратора (пользователь создается по умолчанию), если не менялись соответствующие параметры в окружении:

```
Name: name_admin
Email: email_admin@admin.admin
Password: password_admin
```