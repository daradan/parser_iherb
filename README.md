## Scraping (parsing) iHerb - health products
You can see how the script works here:
- [iHerb deals Kazakhstan](https://t.me/iherb_deals)

The script scrapes (parses) the site and adds information about the products to the database. The next time the script runs, it checks the products and if the price changes, it adds a new price to the database. If the price has decreased equally or less than 15%, it sends a notification to the Telegram channel.

### Installation and setup
Clone repositories
```
git clone https://github.com/daradan/parser_iherb.git
```
Installing libraries
```
pip install -r requirements.txt
```
Create file ___.env___ and fill in your data
```
PLATFORM=...
USER_AGENT=...
TG_CHANNEL=@...
TG_CHANNEL_ERROR=...
TG_TOKEN=...
RCODE=...
```

## Скрейпинг (парсинг) iHerb - товары для здоровья
Работу скрипта можно посмотреть тут:
- [iHerb скидки Казахстан](https://t.me/computeruniverse_deals)

Скрипт скрейпит (парсит) сайт и добавляет в БД информацию о товарах. При следующем запуске проверяет товар, и в случае изменения цены добавляет новую цену в БД. Если цена снизилась равно или меньше на 15%, то отправляет уведомление на Telegram-канал.

### Установка и настройка
Клонируем репозитории
```
git clone https://github.com/daradan/parser_CU.git
```
Устанавливаем библиотеки
```
pip install -r requirements.txt
```
Создаем файл ___.env___ и заполняем свои данные
```
PLATFORM=...
USER_AGENT=...
TG_CHANNEL=@...
TG_CHANNEL_ERROR=...
TG_TOKEN=...
RCODE=...
```
