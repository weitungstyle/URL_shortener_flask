from flask_pymongo import PyMongo
from flask import current_app


class URLModel:
    def __init__(self):
        self.mongo = PyMongo(current_app)

    def create_short_url(self):
        import string
        import random

        letters = string.ascii_lowercase
        short_url = ''.join(random.choice(letters) for i in range(6))
        return short_url

    def create_url(self, original_url):
        url_data = {'url': original_url, 'shortenUrl': self.create_short_url()}
        inserted_id = self.mongo.db.urls.insert_one(url_data).inserted_id
        return inserted_id

    def get_url(self, short_url):
        url = self.mongo.db.urls.find_one({'short_url': short_url})
        return url
