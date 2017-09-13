# PytSite Currency HTTP API


## GET currency/list

Получение списка валют.


### Формат ответа

- **str** `CODE`. Трёхсимвольный код валюты по [ISO 4217](https://ru.wikipedia.org/wiki/ISO_4217).
    - **str** `title`. Название.
    - **str** `symbol`. Символ.


### Примеры

Запрос:

```
curl -X GET \
-H 'PytSite-Auth: e51081bc4632d8c2a31ac5bd8080af1b' \
http://test.com/api/1/currency/list
```

Ответ:

```
{
    "UAH":
    {
        "title": "Украинская гривна",
        "symbol": "₴"
    },
    "USD":
    {
        "title": "Доллар США",
        "symbol": "$"
    }
}
```
