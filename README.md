Quora API
=========

An unofficial API for Quora.

### Table of Contents
* [API Usage](#api-usage)
* [Features](#features)
* [Installation](#installation)
* [Contributing](#contributing)

**Note: The new Quora UI revamp breaks this API, so whenever that goes public for guests, parts of the API will need to be rewritten.**

# API Usage
### API Base URL: `http://quora-api.herokuapp.com`

## GET: `/users/<user>`
### Example
Example usage: `GET http://quora-api.herokuapp.com/users/Christopher-J-Su`

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

## GET: `/users/<user>/activity`
### Example
Example usage: `GET http://quora-api.herokuapp.com/users/Christopher-J-Su/activity`

Output (excerpt):

    {
      "activity": [
        <-- ... --->
        {
          "link": "http://www.quora.com/University-of-Washington/What-does-the-UW-CS-department-gain-from-barring-other-UW-students-from-taking-its-courses/answer/Christopher-J-Su", 
          "published": "Tue, 25 Feb 2014 00:10:55 GMT", 
          "summary": "<-- ... --->", 
          "title": "What does the UW CS department gain from barring other UW students from taking its courses?"
        }, 
        {
          "link": "http://www.quora.com/Can-applied-math-students-take-CSE-majors-only-courses/answer/Christopher-J-Su", 
          "published": "Tue, 25 Feb 2014 00:04:33 GMT", 
          "summary": "<div style=\"color: #666666;\">Christopher J. Su added this answer.</div><br /><div id=\"ld_ihbjvp_3370\"><div style=\"font-weight: bold; color: #000000;\"><div class=\"hover_menu hidden hover_menu_wide hover_menu_cards\" id=\"__w2_qIjTQfx_menu\" style=\"display: none;\"><div class=\"hover_menu_nub\"></div><div class=\"hover_menu_contents\" id=\"__w2_qIjTQfx_menu_contents\"> </div></div><a class=\"user\" href=\"http://www.quora.com/Christopher-J-Su\" id=\"__w2_qIjTQfx_link\">Christopher J. Su</a></div><br />I think you might need to fill out a CSE course petition to take a 300+-level CSE course as a non-major: <span class=\"qlink_container\"><a class=\"external_link\" href=\"https://www.cs.washington.edu/prospective_students/undergrad/petition/\" target=\"_blank\">Petition for Non-Majors</a></span>.<br /><br /><a href=\"http://www.quora.com/Can-applied-math-students-take-CSE-majors-only-courses\" style=\"font-weight: bold;\">See question on Quora</a></div>", 
          "title": "Can applied math students take CSE majors only courses?"
        }
        <-- ... --->
      ], 
      "last_updated": "Thu, 24 Jul 2014 05:32:49 GMT", 
      "username": "Christopher-J-Su"
    }

# Features
### Currently implemented
* User statistics
* User activity

### Todo
* Questions and answers
* Detailed user information (followers, following, etc.; not just statistics)
* Unit tests
* Memcached

# Installation
If you want to run the API locally:

    $ pip install -r requirements.txt
    $ python server.py

# Contributing
Feel free to submit a pull request or an issue!