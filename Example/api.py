#!/usr/bin/env python3
# coding:utf-8
from flask import Flask, jsonify, request
import pymongo
import os
from os.path import join, dirname
from dotenv import load_dotenv

app = Flask(__name__)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
Mongo_URL = os.environ.get("MONGO_ADDRESS") 

@app.route("/")
def hello():

    result = {
        "Result": "Hello World"
    }

    return jsonify(result)

# Receive POST JSON DATA FROM POSTMAN
# INSERT TO MongoDB study Database Hello_World Collection
@app.route("/api/insert", methods=['POST'])
def insert_db():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error')
    else:
        print(Mongo_URL)
        client = pymongo.MongoClient(Mongo_URL)
        db = client['study']
        co = db['Hello_World']
        co.insert(request.json)

    return jsonify(res='ok')


if __name__ == "__main__":
    app.run(debug=True)