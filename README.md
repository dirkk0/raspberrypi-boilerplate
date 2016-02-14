Installation
============

Install flask-restful (this also installs flask):
`sudo pip install flask-restful`

Run with `python restserver.py` and navigate to `http://pi:8000`.

To run in background use screen:

`screen -S server -L -dm bash -c "python restserver.py"`

How it works
============

`restserver.py` implements a RESTful Flaskserver with a tiny example API where `http://pi:8000/radio/1` starts an internet radio stream, while `http://pi:8000/radio/stop` stops it. `runner.py` manages a singleton process, so that this can be controlled from any device (you can start it on one and stop it on another). In `static/index.html` is some minimal Ajax code to control the API.


Known problems
==============
If something hangs, type `killall omxplayer.bin`.