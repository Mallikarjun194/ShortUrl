# #!/usr/bin/env python
# # encoding: utf-8
import json
from flask import Flask, jsonify, request
import random, string
app = Flask(__name__)
url = {}


@app.route('/get', methods=['GET'])
def get_short_url():
    with open('shorturl.json', 'r') as f:
        data = f.read()
        file = json.loads(data)
        record = json.loads(request.data)
        for rec in file:
            if rec['url'] == record['url']:
                return jsonify({record['url']: rec[record['url']]})

        else:
            return jsonify({"Error_msg": "url not found, Please do a POST call"})


@app.route('/create', methods=['POST', 'PUT'])
def create_record():
    record = json.loads(request.data)
    rand_alpha_num = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    # Creating a shorturl like myapp.com/<5-digit Alphanumeric>
    short_url = 'myapp.com/' + rand_alpha_num
    if request.method == 'POST':
        with open('shorturl.json', 'r') as f:
            data = f.read()
            if not data:
                file = dict()
                file[record['url']] = short_url
            else:
                file = json.loads(data)
                if record['url'] in file.keys():
                    return jsonify({'Error_msg': "url already present"})
                else:
                    file[record['url']] = short_url
            with open('shorturl.json', 'w') as f:
                f.write(json.dumps(file, indent=2))
            return jsonify(file), 201
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
