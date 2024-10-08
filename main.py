import sys

from add_to_db import add_bookmark_to_notion

if len(sys.argv) == 2:
    url = sys.argv[1]
    add_bookmark_to_notion(url)
