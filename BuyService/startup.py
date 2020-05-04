import json
from collections import namedtuple
from flask import Flask, abort, request, jsonify
from PIL import Image

app = Flask(__name__)

@app.route('/')
def get_demo():
    return "hello wuga"

@app.route('/create', methods=['POST'], strict_slashes=False)
def create_item():
    content = request.files['uploadfile_ant']
    print(content)
    name = request.form['imgIndex']
    image = Image.open(content)
    image.save(r'c:\workspace\tmp')
    return name
