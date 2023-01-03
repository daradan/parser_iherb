from typing import List

import config
from models import IHerbPrices
from schemas import ProductSchema, PriceSchema


def get_images(part_number: str, index: int) -> str:
    part = part_number.split('-')[0].lower()
    number = part_number.split('-')[1]
    image = f"{config.URL_I}{part}/{part}{number}/l/{index}.jpg"
    return image


def fix_price(price: str) -> str:
    price = price.replace(',', '')
    return price[1:]


def get_percentage(price: int, price_old: int) -> str:
    percent = round(-1 * (100 - (price * 100 / price_old)))
    if percent > 0:
        percent = f'+{percent}'
    return str(percent)


def make_image_caption(product_obj: ProductSchema, price_obj: PriceSchema, last_n_prices) -> str:
    fixed_category = fix_category(product_obj.category)
    image_caption = f"<b>{product_obj.name}</b>\n" \
                    f"#{fixed_category} #{product_obj.brand}\n\n" \
                    f"Рейтинг: {product_obj.rating} ({product_obj.rating_count})\n\n" \
                    f"{fix_last_n_prices(last_n_prices)}\n" \
                    f"<a href='{product_obj.url}?rcode={config.RCODE}{make_utm_tags()}'>Купить</a>\n\n" \
                    f"{config.TG_CHANNEL}"
    return image_caption


def fix_category(category: str) -> str:
    need_to_replace = [' ', '-', ',']
    for change in need_to_replace:
        if change in category:
            category = category.replace(change, '_')
    return category


def fix_last_n_prices(last_n_prices: List[IHerbPrices]) -> str:
    last_n_prices_text = ''
    for data_price in last_n_prices:
        month = data_price.created.month
        day = data_price.created.day
        if data_price.discount:
            dscnt = f' ({data_price.discount}%)'
        else:
            dscnt = ''
        if month < 10:
            month = f"0{month}"
        if day < 10:
            day = f"0{day}"
        last_n_prices_text += f'{data_price.created.year}/{month}/{day} - {data_price.price} ₸{dscnt}\n'
    return last_n_prices_text


def make_utm_tags() -> str:
    utm_campaign = config.TG_CHANNEL[1:]
    return f"&utm_source=telegram&utm_medium=messenger&utm_campaign={utm_campaign}&utm_term={config.UTM}"
