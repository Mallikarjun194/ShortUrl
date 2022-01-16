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
    record = json.loads(request.data)
    rand_alpha_num = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    # Creating a shorturl like myapp.com/<5-digit Alphanumeric>
    short_url = 'myapp.com/' + rand_alpha_num
    if request.method == 'POST':
        if record['url'] in url.keys():
            return jsonify({'Error_msg': "url already present"})
        else:
            url[record['url']] = short_url
            return jsonify(url), 201
    else:
        if record['url'] in url.keys():
            url[record['url']] = short_url
            return jsonify(url)
        else:
            return jsonify({'Error_msg': "url not present, Please do a POST call"})


@app.route('/delete', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    if record['url'] in url.keys():
        url.pop(record['url'])
        return jsonify({"Success:": "url deleted successfully"})
    else:
        return jsonify({"Error_msg": "Requested url not found"})


app.run()
