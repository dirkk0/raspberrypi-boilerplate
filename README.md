Installation
============

Either clone this repo or download the zip:

    wget https://github.com/dirkk0/raspberrypi-boilerplate/archive/master.zip
    unzip master.zip
    cd rasperberrypi-boilerplate-master


Install flask-restful (this also installs flask):
`sudo pip install flask-restful`

Run with `python restserver.py` and navigate to `http://pi:5000`.

To run in background use screen:

`screen -S server -L -dm bash -c "python restserver.py"`

You should now be able to start a stream with `curl http://pi:5000/radio/1` and `curl http://pi:5000/radio/stop` should stop the stream (replace 'pi' with name or IP of your pi)

How it works
============

`restserver.py` implements a RESTful Flaskserver with a tiny example API where `http://pi:5000/radio/1` starts an internet radio stream, while `http://pi:8000/radio/stop` stops it. `runner.py` manages a singleton process, so that this can be controlled from any device (you can start it on one and stop it on another). In `static/index.html` is some minimal Ajax code to control the API.


Known problems
==============
If the player hangs (if you close the restserver while omxplayer is still running, for example), type `killall omxplayer.bin`.