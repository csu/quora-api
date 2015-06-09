Quora API
=========

#### Note: this API is currently broken due to changes on Quora's end. Please report issues and make pull requests over at [csu/pyquora](http://github.com/csu/pyquora).

An unofficial API for Quora.

### Table of Contents
* [API Usage](#api-usage)
* [Features](#features)
* [Installation](#installation)
* [Contributing](#contributing)

# API Usage
### API Base URL: `http://quora-api.herokuapp.com`

## Endpoints Summary
* GET: [`/users/<user>`](#get-usersuser)
  * GET: [`/users/<user>/activity`](#get-usersuseractivity)
    * GET: `/users/<user>/activity/answers`
    * GET: `/users/<user>/activity/user_follows`
    * GET: `/users/<user>/activity/want_answers`
    * GET: `/users/<user>/activity/upvotes`
    * GET: `/users/<user>/activity/review_requests`
* GET: [`/questions/<question>`](#get-questionsquestion)

### GET: `/users/<user>`
#### Example
Example usage: `GET http://quora-api.herokuapp.com/users/Christopher-J-Su`

Example result:
```json
{
  "answers": 301, 
  "blogs": null, 
  "edits": 5576, 
  "followers": 173, 
  "following": 167, 
  "name": "Christopher-J-Su", 
  "posts": 6, 
  "questions": 110, 
  "topics": null, 
  "username": "Christopher-J-Su"
}
```
Note: due to recent Quora UI changes, the `blogs` and `topics` statistics are currently not working and will always return `null`.

### GET: `/users/<user>/activity`
Get the user's activity.
#### Example
Example usage: `GET http://quora-api.herokuapp.com/users/Christopher-J-Su/activity`

Output (excerpt):
```json
{
  "activity": [
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
  ], 
  "last_updated": "Thu, 24 Jul 2014 05:32:49 GMT", 
  "username": "Christopher-J-Su"
}
```

### GET: `/users/<user>/activity/answers`
Get the user's latest answers.
#### Example
Example usage: `GET http://quora-api.herokuapp.com/users/Christopher-J-Su/activity/answers`

Output (excerpt):
```json
{
  "items": [
    {
      "id": "5:48afe1749959ac2b673b1094a13b6cb5#1418975956225507", 
      "link": "http://www.quora.com/I-need-a-summer-internship-but-I-dont-want-to-apply-because-theres-a-90-chance-Ill-get-rejected-What-should-I-do/answer/Christopher-J-Su", 
      "published": "Fri, 19 Dec 2014 07:59:16 GMT", 
      "summary": "<div id=\"ld_ftujiv_1299\"><div style=\"font-weight: bold; color: #000000;\"><div class=\"hover_menu hidden hover_menu_cards hover_menu_wide hover_menu_cards\" id=\"__w2_lHemksQ_menu\" style=\"display: none;\"><div class=\"hover_menu_nub\"></div><div class=\"hover_menu_contents\" id=\"__w2_lHemksQ_menu_contents\"> </div></div><a class=\"user\" href=\"http://www.quora.com/Christopher-J-Su\" id=\"__w2_lHemksQ_link\">Christopher J. Su</a></div><br />Apply, interview, fail, repeat. Keep failing. Eventually, you&#039;ll notice you stop failing as much as you did before. Then, you&#039;ll suddenly start passing interviews. Then, you&#039;ll start getting offers.<br /><br />Don&#039;t get locked up in the mindset that you won&#039;t make it. If you never even try, you&#039;ll never get an internship. Having interviews scheduled will motivate you to study and prepare for them. Doing the interviews themselves is great practice.<br /><br /><a href=\"http://www.quora.com/I-need-a-summer-internship-but-I-dont-want-to-apply-because-theres-a-90-chance-Ill-get-rejected-What-should-I-do\" style=\"font-weight: bold;\">See question on Quora</a></div>", 
      "title": "I need a summer internship, but I don't want to apply because there's a 90% chance I'll get rejected. What should I do?"
    }
  ]
}
```

### GET: `/users/<user>/activity/user_follows`
Get the user's latest user follows.
#### Example
Example usage: `GET http://quora-api.herokuapp.com/users/Christopher-J-Su/activity/user_follows`

Output (excerpt):
```json
{
  "items": [
    {
      "id": "4:c219dbf80746802cf733f0cb3d5218c2#1419000196656496", 
      "link": "http://www.quora.com/Inna-Vishik", 
      "published": "Fri, 19 Dec 2014 14:43:16 GMT", 
      "summary": "", 
      "title": "Inna Vishik"
    },
    {
      "id": "4:bd7227ae22f8f8cd9acfcb906ae8f6ea#1418975190093378", 
      "link": "http://www.quora.com/Mira-Zaslove", 
      "published": "Fri, 19 Dec 2014 07:46:30 GMT", 
      "summary": "", 
      "title": "Mira Zaslove"
    }
  ]
}
```

### GET: `/users/<user>/activity/want_answers`
Get the user's latest followed questions.
#### Example
Example usage: `GET http://quora-api.herokuapp.com/users/Christopher-J-Su/activity/want_answers`

Output (excerpt):
```json
{
  "items": [
    {
      "id": "1:03fb57d2ccb343bff9bb608c6978f5c7#1418895552348316", 
      "link": "http://www.quora.com/What-is-a-typical-day-like-for-a-software-engineer-at-Google", 
      "published": "Thu, 18 Dec 2014 09:39:12 GMT", 
      "summary": "<div id=\"ld_veqgnk_1856\"><span id=\"ld_veqgnk_1857\">5 Answers</span><br /><br /><a href=\"http://www.quora.com/What-is-a-typical-day-like-for-a-software-engineer-at-Google\" style=\"font-weight: bold;\">See question on Quora</a></div><br />", 
      "title": "What is a typical day like for a software engineer at Google?"
    }
  ]
}
```

### GET: `/users/<user>/activity/upvotes`
Get the user's latest upvoted answers.
#### Example
Example usage: `GET http://quora-api.herokuapp.com/users/Christopher-J-Su/activity/upvotes`

Output (excerpt):
```json
{
  "items": [
    {
      "id": "5:cf756de40913266d1c7bb0ff1306a384#1419235600718606", 
      "link": "https://www.quora.com/What-criteria-are-Google-interns-graded-on-for-performance-reviews/answer/Kshitij-Gopal", 
      "published": "Mon, 22 Dec 2014 08:06:40 GMT", 
      "summary": "<div id=\"ld_gurtiz_2329\"><div style=\"font-weight: bold; color: #000000;\"><div class=\"hover_menu hidden hover_menu_cards hover_menu_wide hover_menu_cards\" id=\"__w2_EisD67h_menu\" style=\"display: none;\"><div class=\"hover_menu_nub\"></div><div class=\"hover_menu_contents\" id=\"__w2_EisD67h_menu_contents\"> </div></div><a class=\"user\" href=\"https://www.quora.com/Kshitij-Gopal\" id=\"__w2_EisD67h_link\">Kshitij Gopal</a></div><br />I&#039;m not sure on what basis the earlier answer was given, but as someone who managed interns directly at Google I&#039;ll give this one a crack.<br /><br />Interns are evaluated on a number of parameters, most of which are confidential but rest assured there are a range of performance criteria, parameters that measure initiative, enthusiasm, work ethic and finally Googley-ness. Going above and beyond is expected and will help you in your final evaluation, if you&#039;re an aspiring intern then remember that.<br /><br />Just to clarify the other answer completely - there is nothing random about it and certainly no &quot;lottery&quot; system. I&#039;ve seen and filled the evaluation form, at Google not much is left to luck.<br /><br /><a href=\"https://www.quora.com/What-criteria-are-Google-interns-graded-on-for-performance-reviews\" style=\"font-weight: bold;\">See question on Quora</a></div>", 
      "title": "What criteria are Google interns graded on for performance reviews?"
    }
  ]
}
```

### GET: `/users/<user>/activity/review_requests`
Get the user's latest review requests.
#### Example
Example usage: `GET http://quora-api.herokuapp.com/users/Aaron-Ounn/activity/review_requests`

Output (excerpt):
```json
{
  "items": [
    {
      "id": "1:24ee4ef5eff0c53d8247f5a45e83f5e3#1418745295543236", 
      "link": "https://www.quora.com/Reviews-of-Elixir-programming-language", 
      "published": "Tue, 16 Dec 2014 15:54:55 GMT", 
      "summary": "<div id=\"ld_qxesgk_3346\"><span id=\"ld_qxesgk_3347\">0 Answers</span><br /><br /><a href=\"https://www.quora.com/Reviews-of-Elixir-programming-language\" style=\"font-weight: bold;\">Write an answer on Quora</a></div><br />", 
      "title": "Reviews of: Elixir (programming language)"
    }
  ]
}
```

### GET: `/questions/<question>`
Get statistics on a question.
#### Example
Example usage: `GET http://quora-api.herokuapp.com/questions/If-space-is-3-dimensional-can-time-also-be-3-dimensional`

Output:
```json
{
  "answer_count": 6, 
  "topics": [
    "Science, Engineering, and Technology", 
    "Science", 
    "Physical Sciences", 
    "Physics", 
    "Time (physics)"
  ], 
  "want_answers": 7
}
```

# Features
### Currently implemented
* User statistics
* User activity
* Question statistics
* Answer statistics

### Todo
* Detailed user information (followers, following, etc.; not just statistics)
* Unit tests
* Cache data with memcached

# Installation
You will need [Python 2](https://www.python.org/download/). [pip](http://pip.readthedocs.org/en/latest/installing.html) is recommended for installing dependencies.

To run the API locally:
```bash
$ pip install -r requirements.txt
$ python server.py
```

# Contributing
Feel free to submit a pull request or an issue!  
Quora API uses the [pyquora package](https://github.com/csu/pyquora).
