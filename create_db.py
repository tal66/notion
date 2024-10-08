import requests
from config import page_id, headers, create_db_url

parent_page_id = page_id


def create_db(parent_page_id):
    data = {
        'object': 'database',
        'cover': None,
        'icon': None,
        'title': [
            {
                'type': 'text',
                'text': {
                    'content': 'My Bookmarks',
                    'link': None
                },
                'annotations': {
                    'bold': False,
                    'italic': False,
                    'strikethrough': False,
                    'underline': False,
                    'code': False,
                    'color': 'default'
                },
                'plain_text': 'My Links',
                'href': None
            }
        ],
        'description': [],
        'is_inline': True,
        'properties': {
            'URL': {
                'rich_text': {}
            },
            'Created Date': {
                'date': {}
            },
            'Image': {
                'files': {}
            },
            'Tags': {
                'multi_select': {
                    'options': []
                }
            },
            'Description': {
                'rich_text': {}
            },
            'Title': {
                'title': {}
            }
        },
        'parent': {
            'type': 'page_id',
            'page_id': parent_page_id
        },
    }

    response = requests.post(create_db_url, headers=headers, json=data)
    if response.ok:
        print("db created successfully")
    print(response.json())


if __name__ == '__main__':
    create_db(parent_page_id)
