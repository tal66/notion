api_key = ""

page_id = ""  # a database will be created in this page

# db
database_id = ""

# urls
create_db_url = 'https://api.notion.com/v1/databases/'
update_db_url = "https://api.notion.com/v1/pages"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}