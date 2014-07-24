quora-api
=========

An unofficial API for Quora. Currently implemented: Users.

# API
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