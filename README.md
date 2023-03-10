# Куда пойти — Москва глазами Артёма

Сайт о самых интересных местах в Москве. Авторский проект Артёма.

![site.png](.gitbook/assets/site.png)

## Демо-версия сайта
Доступна по ссылке: [WhereToGo](https://egoista.pythonanywhere.com/)

Администрирование сайта: [Тут](https://egoista.pythonanywhere.com/admin/)

## Запуск

- Рекомендуется использовать виртуальное окружение для запуска проекта
- Для корректной работы Вам необходим Python версии 3.6 и выше
- Скачайте код
- Установите зависимости командой
```bash
pip install -r requirements.txt
```
- Создайте файл базы данных и сразу примените все миграции командой
```bash
python manage.py migrate
```
- Запустите сервер командой
```bash
python manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, 
создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком 
формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:
- `DEBUG` — режим отладки. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — смотри [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

## Добавление новых локаций

Для добавления новых локаций можно использовать [панель администратора](https://egoista.pythonanywhere.com/admin/) 
или использовать команду из терминала:
* Для загрузки локального JSON файла:
```bash
python manage.py load_place --file my_place.json
```

* Для загрузки JSON файла по внешней ссылке:
```bash
python manage.py load_place --url http://example.com/my_place.json
```

*Для пропуска загрузки картинок используйте:*

```bash
python manage.py load_place --file my_place.json --skip_imgs
```

### Формат JSON файла

Для корректной работы скрипта необходим следующий формат JSON файла:

```json
{
    "title": "Название места",
    "imgs": [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg"
    ],
    "description_short": "Краткое описание места",
    "description_long": "Полное описание локации. Допускается использование html-разметки.",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

## Цели проекта

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
