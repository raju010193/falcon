from mongoengine import *


class Product(Document):
    name = StringField(max_length=230, required=True)
    content = StringField(required=True)
