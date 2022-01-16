# #!/usr/bin/env python
# # encoding: utf-8
import os.path as path
import json
from flask import Flask, jsonify, request
import random, string
app = Flask(__name__)


def read_file():
    with open('shorturl.json', 'r') as f:
        data = f.read()
        return data


def write_file(data):
    with open('shorturl.json', 'w') as f:
        f.write(json.dumps(data, indent=2))


@app.route('/get', methods=['GET'])
def get_short_url():
    file = read_file()
    data = json.loads(file)
    param = request.args.get('url')
    if param in data:
        return jsonify({param: data[param]})
    else:
        return jsonify({"Error_msg": "url not found, Please do a POST call"})


@app.route('/create', methods=['POST', 'PUT'])
def create_record():
    record = json.loads(request.data)
    rand_alpha_num = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    short_url = 'myapp.com/' + rand_alpha_num
    file1 = read_file()
    if not file1:
        data = dict()
        data[record['url']] = short_url
    else:
        data = json.loads(file1)
        if record['url'] in data.keys():
            return jsonify({'Error_msg': "url already shortened " + data[record['url']]})
        else:
            data[record['url']] = short_url
    write_file(data)
    return jsonify({"Success": "Your short url is "+data[record['url']]}), 201


@app.route('/update', methods=['PUT'])
def update_method():
    record = json.loads(request.data)
    rand_alpha_num = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    short_url = 'myapp.com/' + rand_alpha_num
    file1 = read_file()
    data = json.loads(file1)
    if record['url'] in data.keys():
        data[record['url']] = short_url
    else:
        return jsonify({"Error_msg": "url not present, Please do a POST call"})
    write_file(data)
    return jsonify({"Success": "Your updated short url is " + data[record['url']]}), 201


@app.route('/delete', methods=['DELETE'])
def delete_record():
    file1 = read_file()
    data = json.loads(file1)
    record = json.loads(request.data)
    if record['url'] in data:
        data.pop(record['url'])
    else:
        return jsonify({"Error_msg": "url not found, Please do a POST call"})
    write_file(data)
    return jsonify({"Success:": "url deleted successfully "+ record['url']})


if not path.exists("shorturl.json"):
    write_file(dict())
app.run(debug=True, host="0.0.0.0")
