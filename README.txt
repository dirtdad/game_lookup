DESCRIPTION
-----------
game_lookup is a python script that returns the "Top Playstation 4 Games" list
from Metacritic's Playstation 4 portal, 
https://www.metacritic.com/game/playstation-4. game_lookup will also look up a 
title in that list.

game_lookup returns its results though a RESTful API. 

GET requests to /games return an array of JSON objects of the format
	[
	{	
		"title": "Persona 5",
		"score": 94
	},
	{
		"title": "Horizon: Zero Dawn",
		"score": 89
	}
	]

GET requests to /games/<title>
where <title> is a URL encoded game name, using %20 for spaces, etc.,
return a single JSON object as shown in the array above, i.e.
	{
		"title": "Nioh",
		"score": 88
	}

REQUIREMENTS
------------
game_lookup requires python 2.7.5 or above, flask, and BeautifulSoup4
and virtualenv installed using pip.

game_lookup listens on port 80, and thus needs to be run with root/admin
privileges.

UNIT TESTING
------------
game_lookup includes 3 modules, each of which include unit tests with
assertions and may also print additional information that is not 
tested by assertion.

To perform unit testing on sub modules, simply invoke them with python 
python get_html.py
python top_titles.py

Some unit tests depend on the external website for testing, "example.com" 
which must include the text "Examnple Domain". Establishing an internally
hosted site for unit testing would be better.

To perform unit testing on the main module, game_lookup, edit the script by
swapping the comments of the last two lines of the script:

        #unittest.main()
        app.run(port=80, debug=True)

will run the script normally, and 

        unittest.main()
        #app.run(port=80, debug=True)

will run a series of 3 unit tests on the script. Then run game_lookup as
described below:

RUNNING AND INVOKING THE API
----------------------------
To run game_lookup, simply run the command as root/admin. It will listen
on port 80 and look somethink like this (lines starting with $ are 
command line input, and are followed by example output):

$ sudo ./game_lookup
 * Serving Flask app "game_lookup" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:80/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 328-827-295

Once the script is running, there are many ways way to use the API. One way
is with the curl command on the same host, in another shell/window:

$ curl localhost/games
[
  {
    "score": "97",
    "title": "Red Dead Redemption 2"
  },
  {
    "score": "92",
    "title": "Divinity: Original Sin II - Definitive Edition"
  },
  {
    "score": "90",
    "title": "Astro Bot: Rescue Mission"
  },
  {
    "score": "89",
    "title": "Tetris Effect"
  },
  {
    "score": "87",
    "title": "Marvel's Spider-Man"
  },
  {
    "score": "86",
    "title": "Dragon Quest XI: Echoes of an Elusive Age"
  },
  {
    "score": "85",
    "title": "Hollow Knight: Voidheart Edition"
  },
  {
    "score": "85",
    "title": "Valkyria Chronicles 4"
  },
  {
    "score": "84",
    "title": "428: Shibuya Scramble"
  },
  {
    "score": "84",
    "title": "SoulCalibur VI"
  }
]

$ curl localhost/games/Red%20Dead%20Redemption%202
[
  {
    "score": "97",
    "title": "Red Dead Redemption 2"
  }
]

$ curl localhost/games/Goat%20Simulator
[
  {
    "score": "title not found",
    "title": "Goat Simulator"
  }
]

KNOWN ISSUES
------------
Error checking is not exhaustive, and not all errors result in JSON, for example:

$ curl localhost/games/God of War
[
  {
    "score": "title not found",
    "title": "God"
  }
]
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html><head>.....
