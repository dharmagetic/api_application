# Запуск
1. Установить зависимости `pip install -r requirements.txt`
2. Запустить миграции `python manage.py migrate`
3. Запустить приложение `python manage.py runserver`

# АПИ «Приложение» (Доступно в браузере) 
1. Список приложений: `GET http://127.0.0.1:8000/api-applications/`
2. Детали приложения: `GET http://127.0.0.1:8000/api-applications/id`
3. Создать приложение: `POST http://127.0.0.1:8000/api-applications/`
4. Удалить приложение: `DELETE http://127.0.0.1:8000/api-applications/id`
5. Обновить ключ приложения: `POST http://127.0.0.1:8000/api-applications/id/reset_key`

# АПИ «Клиент»
Сделать запрос в АПИ с использованием ключа приложения:
`curl -H 'Api-Application-Key: key' http://127.0.0.1:8000/api-applications/test/`
