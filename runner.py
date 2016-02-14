
import subprocess
import shlex
import signal

import os
import time


class Runner:

    def __init__(self):
        self.process = None
        ## on ubuntu, install vlc
        # self.player = 'cvlc'
        ## on raspberrypi, omxplayer is already installed
        self.player = 'omxplayer'


    def run(self, cmd):
        self.process = subprocess.Popen(
            shlex.split(cmd),
            shell=False, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def play(self, filename):
        if self.process:
            self.stop()
        cmd = self.player + ' ' + filename
        self.run(cmd)

    def stop(self):
        print self.process.pid
        self.process.stdin.write('q')
        if self.process:
            # os.killpg(os.getpgid(self.process.pid), signal.SIGTERM) 
            os.kill(self.process.pid, signal.SIGTERM) 
            self.process = None

if __name__ == '__main__':
    r = Runner()

    # filename = "test.mp3"
    filename = "http://205.164.62.20:8206"
    r.play(filename)
    time.sleep(2)
    r.stop()
    r.play(filename)
    time.sleep(2)
    r.stop()