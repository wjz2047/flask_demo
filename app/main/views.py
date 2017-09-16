from flask import request, jsonify
from . import main

@main.route('/v1/main/get/<cust_id>', methods = ['GET'])
def test_get(cust_id):
    print('cust_id: %s, type: %s' % (cust_id, type(cust_id)))
    key1 = request.args.get('key1')
    print('key1:', key1, 'type:', type(key1))

    result = {
        'status': 'SUCCESS',
        'data': 'test get'
    }
    return jsonify(result)

@main.route('/v1/main/post', methods = ['POST'])
def test_post():
    post_data = request.form
    if post_data is None:
        post_data = request.json
    print('key1:', post_data['key1'], 'type:', type(post_data['key1']))

    result = {
        'status': 'SUCCESS',
        'data': 'test post'
    }
    return jsonify(result)


