from flask import request, jsonify, g
from . import main
from ..decorator import jsonp, auth

@main.before_request
def before_request():
    print('run this before every request to main module...')


@main.route('/v1/main/get', methods = ['GET'])
@jsonp
@auth.login_required
def test_get():
    print('cust_id:', g.user)
    key1 = request.args.get('key1')
    print('key1:', key1, 'type:', type(key1))

    result = {
        'status': 'SUCCESS',
        'data': 'test get'
    }
    return jsonify(result)

@main.route('/v1/main/post', methods = ['POST'])
@auth.login_required
def test_post():
    post_data = request.get_json()
    if post_data is None:
        post_data = request.form
    if post_data is None:
        result = {
            'status': 'FAILURE',
            'data': 'No Data'
        }
        return jsonify(result)

    print('key1:', post_data['key1'], 'type:', type(post_data['key1']))

    result = {
        'status': 'SUCCESS',
        'data': 'test post'
    }
    return jsonify(result)


