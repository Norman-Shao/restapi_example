#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import request, jsonify
from flask.views import MethodView

from factory import create_app
from models import Post


app = create_app()

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

class PostListView(MethodView):
    def get(self):
        posts = Post.objects.all()
        data = [post.to_dict() for post in posts]

        return jsonify(posts=data)

    def post(self):
        '''
        post data example:
        {
            "title": "Title 1",
            "slug": "title-1",
            "abstract": "Abstract for this article",
            "raw": "The article content",
            "author": "Gevin",
            "category": "default",
            "tags": ["tag1", "tag2"]
        }
        '''
        data = request.get_json()
        article = Post()

        # return jsonify(data)

        article.title = data.get('title')
        article.slug = data.get('slug')
        article.abstract = data.get('abstract')
        article.raw = data.get('raw')
        article.author = data.get('author')
        article.category = data.get('category')
        article.tags = data.get('tags')

        article.save()

        return jsonify(article.to_dict())

app.add_url_rule('/posts/', view_func=PostListView.as_view('posts'))



if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 5000
    )