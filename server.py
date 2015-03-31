#!/usr/bin/env python
from flask import Flask, jsonify, request
from quora import Quora, Activity
import logging
from logging import StreamHandler

file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

app = Flask(__name__)

# log to stderr
import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

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
            'user_activity_votes': '/users/{user}/activity/votes',
            'question': '/questions/{question}',
            'answer': '/answers/{answer_short_link}',
            'answer_with_user': ['/answers/{question}/{user}', '/answers/{question}/answer/{user}']
        }
    })

####################################################################
# Users
####################################################################

@app.route('/users/<user>', methods=['GET'])
def user_stats_route(user):
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
def user_user_follows_route(user):
    return jsonify({'items': Quora.get_activity(user).user_follows})

@app.route('/users/<user>/activity/want_answers', methods=['GET'])
def user_want_answers_route(user):
    return jsonify({'items': Quora.get_activity(user).want_answers})

@app.route('/users/<user>/activity/upvotes', methods=['GET'])
def user_upvotes_route(user):
    return jsonify({'items': Quora.get_activity(user).upvotes})

@app.route('/users/<user>/activity/review_requests', methods=['GET'])
def user_review_requests_route(user):
    return jsonify({'items': Quora.get_activity(user).review_requests})

####################################################################
# Questions
####################################################################
@app.route('/questions/<question>', methods=['GET'])
def question_stats_route(question):
    return jsonify(Quora.get_question_stats(question))

####################################################################
# Answers
####################################################################
@app.route('/answers/<question>/<user>', methods=['GET'])
def answer_stats_specific_user_route(question, user):
    return jsonify(Quora.get_one_answer(question, user=user))

@app.route('/answers/<question>/answer/<user>', methods=['GET'])
def answer_stats_specific_user_alternate_route(question, user):
    return jsonify(Quora.get_one_answer(question, user=user))

@app.route('/answers/<answer_short_link>', methods=['GET'])
def answer_stats_short_link_route(answer_short_link):
    return jsonify(Quora.get_one_answer(answer_short_link))

####################################################################
# Start Flask
####################################################################
if __name__ == '__main__':
    app.run(debug=True)
