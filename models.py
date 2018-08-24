# -*- coding: utf-8 -*-

from exts import db

post_tag = db.Table('post_tag', db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return f'<User {self.name}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('posts'))
    tags = db.relationship('Tag', secondary=post_tag, backref=db.backref('posts'))

    def __init__(self, title, content, author_id):
        self.title = title
        self.content = content
        self.author_id = author_id

    def __repr__(self):
        return f'<Post {self.title}>'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Tag {self.name}>'
