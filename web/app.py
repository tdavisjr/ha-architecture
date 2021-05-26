import os
import redis

from flask import Flask, json, jsonify, render_template
from flask_pymongo import PyMongo


app = Flask(__name__)

server_name = os.environ['SERVER_NAME']

app.config["MONGO_URI"] = "mongodb://mongo0:27017,mongo1:27017,mongo2:27017/test?replicaSet=rs0&readPreference=secondaryPreferred"
mongo = PyMongo(app)

cache = redis.Redis(host='redis', port=6379, password='')


@app.route("/")
def hello_world():
    users_list = []
    users = mongo.db.users.find({})
    for user in users:
        users_list.append(user['firstName'])

    return render_template('index.j2', users=users_list)
