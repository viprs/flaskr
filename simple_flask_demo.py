#!/usr/bin/python
#encoding:utf-8
"""最简单的Flask应用"""
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "index page"
    
@app.route("/users/")
def get_users():
    return "all users"

if __name__ == "__main__":
    app.run(debug=True)