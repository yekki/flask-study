# -*- coding: utf-8 -*-

from flask import Flask
from exts import db
from models import User, Post

import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    # u1 = User.query.filter(User.id == 1).first()
    # post3 = Post('hello3', 'world3', author_id=u1.id)

    p1 = Post.query.filter(Post.id == 1).first()
    u1 = User.query.filter(User.id == 1).first()

    for p in u1.posts:
        print(p.title)

    return f"hello world {p1.author.name}"


if __name__ == '__main__':
    app.run(debug=True)
