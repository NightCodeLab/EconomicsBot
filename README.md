# EconomicsBot
Бот для учета расходов. Проект являеться примером работ код-студии [NightCodeLab](https://t.me/nightcodelab).

### Запуск
В файле ```bot/config.py``` смените ```TOKEN``` на токен вашего бота. Его можно получить [тут](https://t.me/BotFather). Если вы загрузили API на собственный сервер, в этом же файле поменяйте ```API_URL``` на url вашего сервера (если порт не указан, по стандарту будет отправляться запрос на порт:80)

Далее выполните эти команды в терминале:

- *Запуск API*
```
pip install -r requirements.txt
python app.py
```
- *Запуск Бота*
```
cd bot
python bot.py
```

Бот работает с базой данных SQLite. Для открытия такой базы можно использовать программу [DB Browser for SQLite](https://sqlitebrowser.org/). Путь к базе данных ```instance/economic.db```
