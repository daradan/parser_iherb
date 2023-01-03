import logging
import requests
from random import randrange, shuffle
from time import sleep

import categories
import config
import send_to_tg
import utils
from crud import IHerbProductsCrud, IHerbPricesCrud
from database import SessionLocal
from schemas import ProductSchema, PriceSchema


class IHerbParser:
    def __init__(self):
        self.session = requests.Session()
        self.db_session = SessionLocal()
        self.products_crud: IHerbProductsCrud = IHerbProductsCrud(session=self.db_session)
        self.prices_crud: IHerbPricesCrud = IHerbPricesCrud(session=self.db_session)

    def start(self):
        logging.info(f"{config.MARKET} Parser Start")
        all_categories = categories.get_categories(self.session)
        shuffle(all_categories)
        for category in all_categories:
            page = 1
            response = self.get_response(category, page)
            if not response:
                continue
            products: list = response['data']['products']
            total_products: int = response['data']['totalSize'] - config.LIMIT
            while total_products > 0:
                page += 1
                total_products -= config.LIMIT
                sleep(randrange(3, 20))
                append = self.get_response(category, page)
                if not append:
                    continue
                products.extend(append['data']['products'])
            self.parse_products(products, category)

    def get_response(self, category: dict, page: int) -> dict | None:
        json_data: dict = config.JSON_DATA
        json_data['categoryIds'].append(str(category['id']))
        json_data['page'] = page
        json_data['pageSize'] = config.LIMIT
        json_data['sort'] = 2
        headers = config.HEADERS
        headers['Host'] = config.URL_P.split('/')[2]
        response = self.session.post(config.URL_P, headers=headers, json=json_data, params=config.PARAMS)
        if response.status_code != 200:
            logging.exception(f"{config.MARKET}, {category}, ERROR: {response}")
            return None
        return response.json()

    def parse_products(self, products: list, category: dict):
        for product in products:
            if not product.get('productId') \
                    or not product.get('displayName') \
                    or not product.get('url') \
                    or not product.get('discountPrice') \
                    or not product.get('partNumber') \
                    or not product.get('primaryImageIndex'):
                logging.info(f"{config.MARKET} - 'displayName' | 'url' | 'discountPrice' | 'partNumber' | "
                             f"'primaryImageIndex' are missing")
                continue
            product_obj = {
                'name': product['displayName'],
                'url': product['url'],
                'store_id': product['productId'],
                'category': category['name'],
                'images': utils.get_images(product['partNumber'], product['primaryImageIndex']),
                'brand': product['brandCode'],
                'rating': product['rating'],
                'rating_count': product['ratingCount'],
                'rating_url': product['ratingUrl'],
                'review_url': product['reviewUrl'],
            }
            product_obj = ProductSchema(**product_obj)
            price = utils.fix_price(product['discountPrice'])
            price_obj = PriceSchema(price=price)
            self.check_data_from_db(product_obj, price_obj)

    def check_data_from_db(self, product_obj: ProductSchema, price_obj: PriceSchema):
        product = self.products_crud.get_or_create(product_obj)
        price_obj.product_id = product.id
        last_price = self.prices_crud.get_last_price(product.id)
        if last_price:
            discount = utils.get_percentage(int(float(price_obj.price)), int(float(last_price.price)))
            price_obj.discount = discount
        if not last_price or price_obj.discount != '0':
            self.prices_crud.insert(price_obj)
            if int(price_obj.discount) <= -15:
                last_n_prices = self.prices_crud.get_last_n_prices(product.id)
                image_caption = utils.make_image_caption(product_obj, price_obj, last_n_prices)
                send_tg = send_to_tg.send_as_photo(image_caption, product_obj.images)
                if send_tg != 200:
                    return


if __name__ == '__main__':
    logging.basicConfig(
        handlers=[logging.FileHandler('../iHerb_parser.log', 'a+', 'utf-8')],
        format="%(asctime)s %(levelname)s:%(message)s",
        level=logging.INFO,
    )
    IHerbParser().start()
