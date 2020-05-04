import uuid


from CosmosDB.image_tool import read_single_disk, image_encoder


def get_item_1():
    item_1 = {
        'id': '1_' + str(uuid.uuid4()),
        'category': 'A',
        'name': 'Andersen',
        'url': 'http:/123',
        'link': 'http:/456',
        'description': 'WA5',
        'picture': image_encoder(read_single_disk('C:\\Users\\zcheh\\Pictures\\Capture.PNG')),
        'price': '15',
        'datetime': '2010-04-04'
   }
    return item_1


def get_item_2():
    item_2 = {
        'id': '2_' + str(uuid.uuid4()),
        'category': 'A',
        'name': 'Andersen',
        'url': 'http:/2123',
        'link': 'http:/2456',
        'description': 'WA5',
        'picture': 'WA5',
        'price': '15',
        'datetime': '2010-04-05'
   }
    return item_2


