from flask import jsonify
from flask import request 
from flask import Blueprint
import requests
from . import api 

@api.route('/todos', methods=['GET', "POST"])
def todos():
    if request.method == 'POST':
        res = requests.post('https://hooks.slack.com/services/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', json={
            'text' : 'This is a message from incoming webhook'
        }, headers={'Content-Type': 'application/json'})
    elif request.method == 'GET':
        pass
    data = request.get_json()
    return jsonify(data)

@api.route('/test', methods=["POST"])
def test():
    res = request.form['text']
    print(res)
    return jsonify(res)
