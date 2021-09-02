# Обрезка ссылок с помощью сервиса Bitly

Это программа, которая при введении длинной ссылки сокращает ее, а при введении битлинка выводит количество кликов по нему.

### Как установить

В папке проекта создайте файл ```.env``` и поместите в него свой токен от сервиса Bitly в переменную ```BITLY_TOKEN```:
```
BITLY_TOKEN="mybitlytoken"
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Примеры запуска

Для запуска проекта используйте команду в папке проекта и вставьте свою ссылку на месте `<link>`:
```
python main.py <link>
```
Если вы хотите сократить ссылку - подставьте вместо `<link>` длинную ссылку, если хотите получить количество кликов - подставьте битлинк.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).