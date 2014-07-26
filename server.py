#!/usr/bin/env python
from flask import Flask, jsonify, request
from pyquora import Quora, Activity

app = Flask(__name__)

####################################################################
# Routes
####################################################################

@app.route('/', methods=['GET'])
def index_route():
    return jsonify({
        'author': 'Christopher Su',
        'author_url': 'http://christophersu.net',
        'base_url': 'http://quora-api.herokuapp.com',
        'project': 'Quora API',
        'project_url': 'https://github.com/csu/quora-api'
    })

####################################################################
# Users
####################################################################

@app.route('/users/<user>', methods=['GET'])
def user_route(user):
    return jsonify(Quora.get_user_stats(user))

@app.route('/users/<user>/activity', methods=['GET'])
def user_activity_route(user):
    return jsonify(Quora.get_user_activity(user))

@app.route('/users/<user>/answers', methods=['GET'])
def user_answers_route(user):
    return jsonify({'items': Quora.get_activity(user).answers})

@app.route('/users/<user>/questions', methods=['GET'])
def user_questions_route(user):
    return jsonify({'items': Quora.get_activity(user).questions})

@app.route('/users/<user>/question_follows', methods=['GET'])
def user_question_follows_route(user):
    return jsonify({'items': Quora.get_activity(user).question_follows})

@app.route('/users/<user>/votes', methods=['GET'])
def user_votes_route(user):
    return jsonify({'items': Quora.get_activity(user).upvotes})

####################################################################
# Start Flask
####################################################################
if __name__ == '__main__':
    app.run(debug=True)