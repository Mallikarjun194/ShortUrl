# #!/usr/bin/env python
# # encoding: utf-8
import json
from flask import Flask, jsonify, request
import random, string
app = Flask(__name__)
url = {}


@app.route('/get', methods=['GET'])
def get_short_url():
    record = json.loads(request.data)
    if record['url'] in url.keys():
        return jsonify({record['url']: url[record['url']]})
    else:
        return jsonify({"Error_msg": "url not found, Please do a POST call"})


@app.route('/create', methods=['POST', 'PUT'])
def create_record():
    pass


@app.route('/delete', methods=['DELETE'])
def delete_record():
    pass


app.run()
