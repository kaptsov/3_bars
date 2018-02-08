# Ближайшие бары

Скрипт анализирует файл json, полученный на [data.mos.ru](https://devman.org/fshare/1503831681/4/), в котором содержится информация о барах Москвы и выводит на экран самый большой, самый маленький и самый ближайший бар, основываясь на данных о количестве мест в заведении и gps-координатам.

# Установка

Скрипт требует для своей работы установленный интерпретатор Python версии 3.5. Затем установите необходимые модули:
```bash
pip install requirements.txt

```
Также требуется скачанный [файл с данными о барах](https://devman.org/fshare/1503831681/4/), его необходимо положить в одну папку со скриптом.

# Как запустить

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
Input longitude, latitude:37.635709999610876 55.805575000158532
The biggest bar is Спорт бар «Красная машина»
The smallest bar is БАР. СОКИ
The closest bar is Бар «Джонни Грин Паб»

```
Обратите внимание, что вводить координаты следует через пробел.

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
