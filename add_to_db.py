import requests

from bookmark import Bookmark
from config import headers, database_id, update_db_url


def prepare_db_data(database_id, bookmark):
    properties = bookmark.get_notion_properties()

    data = {
        "parent": {"type": "database_id", "database_id": database_id},
        "properties": properties
    }

    return data


def send_to_db(data):
    response = requests.post(update_db_url, headers=headers, json=data)
    if response.status_code == 200:
        print("db updated successfully")
    else:
        print(f"Failed to update block. Status code: {response.status_code}")
    return response


def add_bookmark_to_notion(url: str):
    bookmark = Bookmark.from_url(url)
    print(bookmark.title)
    data = prepare_db_data(database_id, bookmark)
    send_to_db(data)


if __name__ == '__main__':
    for url in ['https://github.com/', 'https://www.reddit.com/', 'https://en.wikipedia.org/wiki/Computer']:
        add_bookmark_to_notion(url)
