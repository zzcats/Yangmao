import json
from collections import namedtuple
from flask import Flask, abort, request, jsonify
app = Flask(__name__)

@app.route('/')
def get_demo():
    return "hello wuga"
