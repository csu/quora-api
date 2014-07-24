#!/usr/bin/env python
from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

####################################################################
# Helpers
####################################################################
def get_count(element):
    try:
        return int(element.find('span', class_='profile-tab-count').string)
    except ValueError:
        return element.find('span', class_='profile-tab-count').string

def get_count_for_user_href(soup, user, suffix):
    return get_count(soup.find('a', class_='link_label', href='/' + user + '/' + suffix))

####################################################################
# Routes
####################################################################

@app.route('/', methods=['GET'])
def index_route():
    return jsonify({'author': 'Christopher Su'})

####################################################################
# Users
####################################################################

@app.route('/users/<user>', methods=['GET'])
def user_route(user):
    soup = BeautifulSoup(requests.get('http://www.quora.com/' + user).text)
    user_dict = { 'username': user }
    user_dict['name'] = soup.find('h1').find('span', class_='user').string
    attributes_to_href_suffix = {
        'followers': 'followers',
        'following': 'following',
        'topics': 'topics',
        'blogs': 'blogs',
        'posts': 'all_posts',
        'questions': 'questions',
        'answers': 'answers',
        'edits': 'log'
    }
    for attribute, suffix in attributes_to_href_suffix.iteritems():
        try:
            user_dict[attribute] = get_count_for_user_href(soup, user, suffix)
        except:
            pass
    return jsonify(user_dict)

####################################################################
# Start Flask
####################################################################
if __name__ == '__main__':
    app.run(debug=True)