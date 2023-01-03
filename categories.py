import requests
import config


def get_categories(session) -> list:
    response = session.post(config.URL_C, headers=config.HEADERS, json=config.JSON_DATA)
    if response.status_code != 200:
        get_categories(session)
    json_loads = response.json()
    categories = []
    for category in json_loads['categories']:
        if category.get('urlName'):
            categories.append(
                {
                    'name': category.get('categoryDisplayName'),
                    'id': category.get('categoryId'),
                    'url': category.get('url')
                }
            )
    return categories


if __name__ == '__main__':
    print(get_categories(requests.Session()))
