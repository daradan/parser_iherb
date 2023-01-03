from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

MARKET = 'iHerb'
TG_CHANNEL = os.getenv('TG_CHANNEL')
TG_TOKEN = os.getenv('TG_TOKEN')
TG_CHANNEL_ERROR = os.getenv('TG_CHANNEL_ERROR')
UTM = ''
RCODE = os.getenv('RCODE')

URL_C = 'https://catalog.app.iherb.com/deal/specials/carousels'
URL_P = 'https://pal.app.iherb.com/api/v1/products/deal/specials'
URL_I = 'https://cloudinary.images-iherb.com/image/upload/f_auto,q_auto:eco/images/'

LIMIT = 24
LAST_N_PRICES = 10

HEADERS = {
    'Host': 'catalog.app.iherb.com',
    'accept-language': 'en-US,en;q=0.8',
    'platform': os.getenv('PLATFORM'),
    'regiontype': 'GLOBAL',
    'ih-pref': 'lc=ru-RU;cc=KZT;ctc=KZ;wp=kilograms',
    'pref': '{"ctc":"KZ","crc":"KZT","crs":"2","lac":"ru-RU","storeid":0,"som":"kilograms"}',
    'user-agent': os.getenv('USER_AGENT'),
    'content-type': 'application/json; charset=UTF-8',
}

JSON_DATA = {
    'attributeValueIds': [],
    'brandCodes': [],
    'categoryIds': [],
    'discountValueRange': [],
    'healthTopicIds': [],
    'includeDiscontinued': False,
    'includeOutOfStock': True,
    'priceRanges': [],
    'programs': [],
    'searchWithinKeyWord': '',
    'showITested': False,
    'showShippingSaver': False,
    'sort': -9999,
    'specials': '',
    'weights': [],
}

PARAMS = {
    'isMobile': 'true',
    'isNative': 'true',
}

json_data = {
    'attributeValueIds': [],
    'brandCodes': [],
    'categoryIds': [
        '1855',
    ],
    'discountValueRange': [],
    'healthTopicIds': [],
    'includeDiscontinued': False,
    'includeOutOfStock': True,
    'page': 1,
    'pageSize': 24,
    'priceRanges': [],
    'programs': [],
    'searchWithinKeyWord': '',
    'showITested': False,
    'showShippingSaver': False,
    'sort': 2,
    'specials': '',
    'weights': [],
}