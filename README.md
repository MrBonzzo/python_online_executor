# Python online executor

## Запуск
Для запуска необходимо ввести следующие команды в терминал:
~~~
docker pull bonzzomi/python_online_executor
docker run -d -p 8000:8000 bonzzomi/python_online_executor
~~~

После запуска приложение будет доступно по адресу `localhost:8000`

## Пример работы
![Пример работы](https://raw.githubusercontent.com/MrBonzzo/python_online_executor/master/example.png)

## Выполнение задания
1) docker контейнер: есть
2) изоляция окружения: сделал через удаление названий конкретных модулей и функций
3) gunicorn в качестве сервера, плюс subprocess.Popen для каждого экземпляра кода
4) приятный интерфейс: есть
5) подсветка синтаксиса: нет
6) таймаут в конфигурационном файле configuration.ini
7) кастомный таймаут: нет
8) создание файлов: нет
9) секьюрность: решилась путём удаления функций из п.2
