from main.database import Database
from main.models import URL_model
from flask import current_app


class URL_handler:
    def __init__(self):
        self.db = Database(current_app)
        self.collection_name = 'urls'

    def post(self, original_url):
        same_url = self.db.duplicated(
            self.collection_name, {"original_url": original_url}
        )
        if same_url:
            return same_url
        else:
            new_url = URL_model(original_url)
            duplicated = self.db.duplicated(self.collection_name, new_url.short_url)
            while duplicated:
                new_url.short_url = new_url.generate()
            data = {
                "original_url": new_url.original_url,
                "short_url": new_url.short_url,
            }
            self.db.insert(self.collection_name, data)
            return new_url.short_url

    def get(self, short_url):
        url = self.db.find_one(self.collection_name, {"short_url": short_url})
        return url["original_url"]
