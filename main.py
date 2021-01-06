######################################################
## This is our Python 'Code Editor'. Write your code in this file! ##
######################################################

from flask import Flask
server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello, World!'


@server.route('/hithere')
def hi_there():
    return 'hithere'

server.run(host='0.0.0.0', debug=True)