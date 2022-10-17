# T20 Cricket World Cup Tipping Competition

#### Video Demo: <url>

A web app built for the CS50 final project, by Ed Bosisto.

### Overview:
Built with Python Django Framework and Sqlite3 backend.
Django templating and Bootstrap 5.2.2 for UX/UI.
The app allows users to register and login with a username and password. 
Users can then "tip" or guess the results of all matches which will be played for the 2022 T20 Cricket World Cup.
Users compete against each other on the "ladder", which shows all users' total correct tips as the competition progresses.

### Files:

#### Templates Folder
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
    
#### tip folder
Contains main app files
###### admin.py
  - 
###### forms.py
  - 
###### models.py
  - 
###### serializers.py
  - 
###### urls.py
  - 
###### views.py
  - 
