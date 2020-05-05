import json
from collections import namedtuple
from flask import Flask, abort, request, jsonify
from storage.storage_client import StorageClient
from constants.key_constants import KeyConstants
from CosmosDB.items import get_item
from CosmosDB.database_dao import get_db_client
import uuid

db_instance = get_db_client()
storage_client = StorageClient(KeyConstants.storage_connect_string, KeyConstants.storage_container)
app = Flask(__name__)


@app.route('/')
def get_demo():
    return "hello wuga"


@app.route('/create', methods=['POST'], strict_slashes=False)
def create_item():
    picture = request.files['uploadfile_ant']
    print(picture.filename)
    blob_picture_path = KeyConstants.storage_url + picture.filename
    local_picture_path = r'c:\workspace\picture_' + picture.filename
    storage_client.upload_file(local_picture_path,blob_picture_path)
    picture.save(local_picture_path)
    name = request.form['itemName']
    detail = request.form['itemDetail']
    item_category = request.form['itemCategory']
    item_price = request.form['itemPrice']
    item = get_item(name, detail, blob_picture_path, item_price, item_category)
    print(item)
    db_instance.add_item(item)
    return name


@app.route('/list', methods=['POST'], strict_slashes=False)
def list_item():
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
