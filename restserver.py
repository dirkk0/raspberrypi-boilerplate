


import urllib2

import runner

runner = runner.Runner()
radios = {
    '1':'http://205.164.62.20:8206',
    '2':'http://217.114.200.100:80',
}


from flask import Flask, request
from flask_restful import Resource, Api

# either this if you have another webserver
# app = Flask(__name__)

# or this to serve static files.
app = Flask(__name__, static_folder='static', static_url_path='')

api = Api(app)
class Radio(Resource):
    def get(self, radio_id):
        runner.play(radios[radio_id])
        return {'msg': 'ok'}


        resp = Flask.make_response("Hello World", 200)
        resp.headers.extend({'X-Powered-By': 'AT-5000'})
        return resp

    # def put(self, radio_id):
    #     todos[radio_id] = request.form['data']
    #     return {radio_id: radios[radio_id]}


def getStation(url):
    req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
    html = urllib2.urlopen(req).read()
    return html.split('Current Song: ')[1] .split('<b>')[1].split('</b>')[0]

class Title(Resource):
    def get(self, radio_id):
        # return getStation(radios[radio_id])
        return {"msg": getStation(radios[radio_id])}


class Stop(Resource):
    def get(self):
        runner.stop()
        return {'msg': 'stop'}


api.add_resource(Radio, '/radio/<string:radio_id>')
api.add_resource(Title, '/title/<string:radio_id>')
api.add_resource(Stop, '/radio/stop')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)