#!/usr/bin/python
#encoding:utf-8

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

app = Flask(__name__)

#config是全局可访问的一个值
app.config.update(dict(
    DATABASE    = os.path.join(app.root_path, 'flaskr.db'),
    DEBUG       = True,
    SECRET_KEY  = 'development key',
    USERNAME    = 'admin',
    PASSWORD    = '123456'
))
def connect_db():
    """连接到数据库文件"""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def get_db():
    """打开"""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/')
def index():
    return "index page"


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)