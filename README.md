# Shop Score Page

В данном проекте реализован дашборд с информацией о максимальном времени ожидания ещё необработанных заявок, количестве необработанных заявок, а также о количестве заказов, обработанных за день. Пример работы можно посмотреть [здесь](http://heroku.com).

## Установка
Перед установкой зависимостей python нужно удостовериться, что в системе установлены пакеты `python3-dev` и  `libpq-dev`. Если они не установлены, то для Debian GNU/Linux и деривативов нужно выполнить:
```bash
apt-get install python3-dev libpq-dev
```
Далее установить зависимости так:
```
pip3 install -r requirements.txt
```


## Запуск
Для запуска выполняем:
```
python3 server.py
```
переходим по [ссылке](http://localhost:5000), готово.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
