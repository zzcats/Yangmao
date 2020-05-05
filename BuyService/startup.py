import json
from collections import namedtuple
from flask import Flask, abort, request, jsonify
from PIL import Image
from CosmosDB.items import get_item
from CosmosDB.database_dao import DatabaseDAO

endpoint = "https://yangmao.documents.azure.com:443/"
key = ''
database_name = 'yangmao'
container_name = "product"
db_instance=DatabaseDAO(endpoint,key,database_name,container_name);

app = Flask(__name__)

@app.route('/')
def get_demo():
    return "hello wuga"

@app.route('/create', methods=['POST'], strict_slashes=False)
def create_item():
    picture = request.files['uploadfile_ant']
    print(picture)
    picture_path = r'c:\workspace\picture_'+picture.filename
    picture.save(picture_path)
    name = request.form['itemName']
    detail = request.form['itemDetail']
    item_category = request.form['itemCategory']
    item_price = request.form['itemPrice']
    item = get_item(name, detail, picture_path, item_price, item_category)
    print(item)
    db_instance.add_item(item)
    return name
