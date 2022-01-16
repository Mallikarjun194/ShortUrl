# #!/usr/bin/env python
# # encoding: utf-8
import json
from flask import Flask, jsonify, request
import random, string
app = Flask(__name__)
url = {}


@app.route('/get', methods=['GET'])
def get_short_url():
    pass


@app.route('/create', methods=['POST', 'PUT'])
def create_record():
    pass


@app.route('/delete', methods=['DELETE'])
def delete_record():
    pass


app.run()
