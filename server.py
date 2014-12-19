#!/usr/bin/env python
from flask import Flask, jsonify, request
from quora import Quora, Activity

app = Flask(__name__)

####################################################################
# Routes
####################################################################

@app.route('/', methods=['GET'])
def index_route():
    return jsonify({
        'author': 'Christopher Su',
        'author_url': 'http://christopher.su',
        'base_url': 'http://quora-api.herokuapp.com',
        'project': 'Quora API',
        'project_url': 'https://github.com/csu/quora-api',
        'project_documentation': 'http://christopher.su/quora-api/',
        'project_issues': 'https://github.com/csu/quora-api/issues',
        'endpoints': {
            'user': '/users/{user}',
            'user_activity': '/users/{user}/activity',
            'user_activity_answers': '/users/{user}/activity/answers',
            'user_activity_questions': '/users/{user}/activity/questions',
            'user_activity_want_answers': '/users/{user}/activity/want_answers',
            'user_activity_votes': '/users/{user}/activity/votes'
        }
    })

####################################################################
# Users
####################################################################

@app.route('/users/<user>', methods=['GET'])
def user_route(user):
    return jsonify(Quora.get_user_stats(user))

####################################################################
# Activity
####################################################################

@app.route('/users/<user>/activity', methods=['GET'])
def user_activity_route(user):
    return jsonify(Quora.get_user_activity(user))

@app.route('/users/<user>/activity/answers', methods=['GET'])
def user_answers_route(user):
    return jsonify({'items': Quora.get_activity(user).answers})

@app.route('/users/<user>/activity/user_follows', methods=['GET'])
def user_questions_route(user):
    return jsonify({'items': Quora.get_activity(user).user_follows})

@app.route('/users/<user>/activity/want_answers', methods=['GET'])
def user_want_answers_route(user):
    return jsonify({'items': Quora.get_activity(user).want_answers})

@app.route('/users/<user>/activity/upvotes', methods=['GET'])
def user_votes_route(user):
    return jsonify({'items': Quora.get_activity(user).upvotes})

####################################################################
# Start Flask
####################################################################
if __name__ == '__main__':
    app.run(debug=True)
