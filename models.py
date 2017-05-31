#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from flask import url_for

import markdown2

from factory import db


class Post(db.Document):
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True, unique=True)
    abstract = db.StringField()
    raw = db.StringField(required=True)
    pub_time = db.DateTimeField()
    update_time = db.DateTimeField()
    content_html = db.StringField()
    author = db.StringField()
    category = db.StringField(max_length=64)
    tags = db.ListField(db.StringField(max_length=30))


    def save(self, *args, **kwargs):
        now = datetime.datetime.now()
        if not self.pub_time:
            self.pub_time = now
        self.update_time = now
        self.content_html = markdown2.markdown(self.raw, extras=['code-friendly', 'fenced-code-blocks', 'tables'])
        
        # print('test:', markdown2.markdown(self.raw, extras=['code-friendly', 'fenced-code-blocks', 'tables']))
        
        return super(Post, self).save(*args, **kwargs)

    def to_dict(self):
        post_dict = {}
        
        post_dict['title'] = self.title
        post_dict['slug'] = self.slug
        post_dict['abstract'] = self.abstract
        post_dict['raw'] = self.raw
        post_dict['pub_time'] = self.pub_time.strftime('%Y-%m-%d %H:%M:%S')
        post_dict['update_time'] = self.update_time.strftime('%Y-%m-%d %H:%M:%S')
        post_dict['content_html'] = self.content_html
        post_dict['author'] = self.author
        post_dict['category'] = self.category
        post_dict['tags'] = self.tags

        return post_dict


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['slug'],
        'ordering': ['-pub_time']
    }