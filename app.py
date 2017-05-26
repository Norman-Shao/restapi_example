#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask 
from flask import request, jsonify
from flask.views import MethodView

app = Flask(__name__)

@app.route('/')
def hello_rest():
    return '''
    <html>
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Code Service</title>
            <link href="//cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container">
                <div class="row">
                    <div class="col-md-8 col-md-offset-2">
                        <h1>Flask RESTful API Example</h1><hr>
                        <p>Welcome to Flask RESTful API Example!</p>
                    </div>
                </div>
            </div>
        </body>
    </html>
    '''

@app.route('/http-method-test/', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def http_method_example():
    if request.method == 'GET':
        return 'Send request with `GET` method'
    elif request.method == 'POST':
        return 'Send request with `POST` method'
    elif request.method == 'PUT':
        return 'Send request with `PUT` method'
    elif request.method == 'PATCH':
        return 'Send request with `PATCH` method'
    elif request.method == 'DELETE':
        return 'Send request with `DELETE` method'
    else:
        return 'Not Allowed HTTP Method', 405 

class HttpMethodExample(MethodView):
    def get(self):
        return 'Send request with `GET` method'

    def post(self):
        return 'Send request with `POST` method'

    def put(self):
        return 'Send request with `PUT` method'

    def patch(self):
        return 'Send request with `PATCH` method'

    def delete(self):
        return 'Send request with `DELETE` method'

class SerializationExample(MethodView):
    def get(self):
        option = request.args.get('option')

        if option == 'list1':
            return self.test_list()
        if option == 'list2':
            return self.test_list2()
        if option == 'dict1':
            return self.test_dict1()
        if option == 'dict2':
            return self.test_dict2()
        if option == 'dict3':
            return self.test_dict3()


        msg = {
            'info': '`option` is needed in url as a url parameter',
            'avilable option values': 'list1, list2, test_dict1, test_dict2, test_dict2'
        }
        return jsonify(msg), 400
        


    def test_list(self):
        data = [{'a':1, 'b':2}, {'c':3, 'd':4}]
        return jsonify(result=data)

    def test_list2(self):
        data = [1,2,3,4,5,6,7,8]
        return jsonify(data)


    def test_dict1(self):
        data = {'a':1, 'b':2, 'c':3}
        return jsonify(data)

    def test_dict2(self):
        data = {'a':1, 'b':2, 'c':3}
        return jsonify(**data)

    def test_dict3(self):
        data = {'a':1, 'b':2, 'c':3}
        return jsonify(result=data)

@app.route('/deserialization/', methods=['get', 'post'])
def deserialization():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return 'No json data found', 400

        result = {
            'json data in request': data
        }
        return jsonify(result)

    return 'Please post json data'

app.add_url_rule('/http-method-test2/', view_func=HttpMethodExample.as_view('http_method_example2'))
app.add_url_rule('/serialization/', view_func=SerializationExample.as_view('serialization'))

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 5000,
        debug = True
    )