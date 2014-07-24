Quora API
=========

An unofficial API for Quora.

### Table of Contents
* [API Usage](#api-usage)
* [Features](#features)

**Note: The new Quora UI revamp breaks this API, so whenever that goes public for guests, parts of the API will need to be rewritten.**

# API Usage
## GET: `/users/<user>`
Example usage: GET `/users/Christopher-J-Su`

Example result:

    {
      "answers": 19, 
      "blogs": 2, 
      "edits": 120, 
      "followers": 6, 
      "following": 64, 
      "name": "Christopher J. Su", 
      "posts": 1, 
      "questions": 8, 
      "topics": 270, 
      "username": "Christopher-J-Su"
    }

# Features
### Currently implemented
* User statistics

### Todo
* User activity
* Questions and answers