# T20 Cricket World Cup Tipping Competition

#### Video Demo: <url>

A web app built for the CS50 final project, by Ed Bosisto.

## Overview:
Built with Python Django Framework and Sqlite3 backend.
Django templating and Bootstrap 5.2.2 for UX/UI.
The app allows users to register and login with a username and password. 
Users can then "tip" or guess the results of all matches which will be played for the 2022 T20 Cricket World Cup.
Users compete against each other on the "ladder", which shows all users' total correct tips as the competition progresses.

## Files:

### Templates Folder
  Templates for all pages on the site.
  - account
    - Logged in users can see a summary of all tips they've saved in the /tips section.
  - base
    - Base template. All .html pages extend this template. Contains html for nav bar, footer, django messages.
  - home
    - Simple home page with login/tip button for users. Upcoming / Today's matches are displayed on the homepage.
  - ladder
    - A table of all registered users, ranking them by their total correct tips. Updated by tally() function in views.py on every visit to the page. Logged in user is highlighted so they can easily identify their position relative to other users.
  - login
    - A simple login form for users to login. Anchor link to Register page if not already signed up.
  - matches
    - A list with details of all matches in the T20 World Cup. Match winner details also appear here as the competition progresses.
  - register
    - Default Django register form for new users. Username, and password confirmation required.
  - tips
    - Logged in users can see a full list of matches, in chronological order, for the T20 Cricket World Cup. If a match has started or has already finished it will not appear in the list for tipping. Users can see their currently saved tip below each match. Tips can be updated by saving a different choice. After each tip is saved, Javascript autoscrolls to the user's last position on the page. This is a UX choice made by me so the user doesn't need to scroll back to their previous position after each selection.
  - static Folder
    - Contains images, css and js folders with static files.
    
### tip Folder
Contains main Django app files
###### admin.py
  - All database models registered. To be viewed and edited in the /admin panel.
###### forms.py
  - Custom form to take user tips. Not used in final deployment.
###### models.py
  - Relational database models.
    - Team, Venue, Match, Tip, Score. See Database below for more information.
###### serializers.py
  - Serializers for Team, Venue, Match models. Not used in final deployment.
###### urls.py
  - Routing patterns for all pages.
###### views.py
  - Functional views used to render all pages. 
    - home
      - Datetime library used to determine next match from match table in database. Next match and Today's match is determined by filtering django querysets on their "when" field, and sent to template for render.
    - account (login required)
      - Logged in user can see a summary of their currently saved tips. User, Tip and Match classes used to determine user's current saved tips.
    - ladder (login required)
      - Tally() function (see below) determines all users' total scores (# correct tips). Score table from database is rendered in template once it's been updated by Tally().
    - loginPage
      - Basic user login, making use of Django's User model. Redirects with error message if already logged in. User inputs are checked and user is logged in with success message if authenticated.
    - logoutUser
      - Makes use of Django's logout() function to log out a user and redirect to the homepage.
    - registerPage
      - UserCreationForm (Django default) is rendered for new users to sign up. Django handles all password protection. Successful registration redirects to homepage with success message.
    - matches
      - all matches from Match table filtered according to what month they occur (October or November) and rendered to a template.
    - tips (login required)
      - filters matches which have already occured using Datetime library.
      - check user is logged in.
      - Get's existing tips for current user from database.
      - When user submits a new tip, form data is retrieved. 
        - Error message and redirect if no team is chosen.
        - Backend check if game has already started / finished. This is to prevent users cheating by leaving the browser open and submitting a tip once the result is known.
        - Check if tip has already been submitted by that user for that match. If exists, update. If doesn't exist, create new entry.
      - Finally, retrieve all tips by current user (again) to update page after a tip is submitted.
  - Tally() function to tally all user scores and update "score" table in database.
    - User class imported from Django.contrib.auth.models. Loops through all users, checking user tips against match winners. Score is tallied, then checked against current user score in database. Updated if score has changed. Tally() runs every time /ladder is viewed.


### Database structure
Sqlite3 database built into Django framework. Models (tables) as follows.
##### Team
  - Basic details for all teams in the world cup.
##### Venue
  - Basic details for all venues to host a match during the world cup (all in Australia).
##### Match
  - team1, team2. Foreign keys from Team table.
  - when. Timestamp, UTC, for match time and date.
  - venue. Foreign key from Venue table.
  - winner. Foreign key from Team table.
##### Tip
  - user_id. Foreign key from Django's User model.
  - match. Foreign key from Match table.
  - tip. Foreign key from Team table.
  - created and updated timestamps.
##### Score
  - user - Foreign key from Django's User model.
  - score - integer field to keep track of user score.
  
