from dataclasses import dataclass
import datetime
import requests
from bs4 import BeautifulSoup


@dataclass
class Bookmark:
    title: str | None = None
    description: str | None = None
    image: str | None = None
    url: str | None = None
    created_date: str | None = datetime.datetime.now(datetime.UTC).isoformat()

    def get_notion_properties(self):
        properties = {"Created Date": {
            "type": "date",
            "date": {"start": self.created_date}
        }}

        if self.title:
            properties["Title"] = {
                "type": "title",
                "title": [{"type": "text", "text": {"content": self.title}}]
            }
        if self.description:
            properties["Description"] = {
                "type": "rich_text",
                "rich_text": [{"type": "text", "text": {"content": self.description, }}]
            }
        if self.image:
            properties["Image"] = {
                "type": "files",
                "files": [
                    {
                        "name": "Article image",
                        "external": {
                            "url": self.image
                        }
                    }
                ]
            }
        if self.url:
            properties["URL"] = {
                "type": "rich_text",
                "rich_text": [{"type": "text",
                               "text": {"content": self.url, "link": {"type": "url", "url": self.url}}}
                              ]
            }

        return properties

    @staticmethod
    def from_url(url) -> "Bookmark":
        response = requests.get(url, headers={
            "Accept-Language": "en-US,en;q=0.9",
        })
        if not response.ok:
            print(response.status_code)
            return Bookmark(url=url)

        soup = BeautifulSoup(response.content, 'html.parser')

        # og tags
        og_title = soup.find("meta", property="og:title")
        og_description = soup.find("meta", property="og:description")
        og_image = soup.find("meta", property="og:image")

        if og_title:
            title = og_title["content"]
        elif soup.title:
            title = soup.title.string
        else:
            title = ""

        if og_description:
            description = og_description["content"]
        else:
            description = soup.find("meta", attrs={"name": "description"})
            if description:
                description = description["content"]
            else:
                description = ""
                p = soup.find("p")
                if p:
                    description = p.text

        description = description.strip()

        image = ""
        if og_image:
            image = og_image["content"]

        return Bookmark(title=title, description=description, image=image, url=url)
