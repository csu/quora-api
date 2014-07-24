#!/usr/bin/env python
from flask import Flask, jsonify, request

app = Flask(__name__)

####################################################################
# Routes
####################################################################

@app.route('/', methods=['GET'])
def index():
    return jsonify({'author': 'Christopher Su'})

####################################################################
# Start Flask
####################################################################
if __name__ == '__main__':
    app.run(debug=True)