#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask 

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

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 5000,
        debug = True
    )