import uuid
import datetime,json


from CosmosDB.image_tool import read_single_disk, image_encoder


def get_item(name,detail,picture_path,price,category):
    item = {
        'id': '1_' + str(uuid.uuid4()),
        'category': category,
        'name': name,
        'url': '',
        'link': 'http:/456',
        'description': detail,
        'picture': picture_path,
        'price': price,
        'datetime': str(datetime.datetime.now())
    }
    return item
