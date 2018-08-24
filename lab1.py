# -*- coding: utf-8 -*-

from flask import Flask
from exts import db
from models import User, Post, Tag

import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    p1 = Post.query.filter(Post.id == 1).first()

    for t in p1.tags:
        print(t)

    return f"hello world {p1.author.name}"


if __name__ == '__main__':
    app.run(debug=True)
