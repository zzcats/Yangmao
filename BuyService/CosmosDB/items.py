import uuid
import datetime


from CosmosDB.image_tool import read_single_disk, image_encoder


def get_item(name,detail,picture,price,category):
    item = {
        'id': '1_' + str(uuid.uuid4()),
        'category': category,
        'name': name,
        'url': 'http:/123',
        'link': 'http:/456',
        'description': detail,
        'picture': image_encoder(picture),
        'price': price,
        'datetime': datetime.datetime.now()
    }
    return item
