from flask import Flask, request, abort
from requests import get
from jsonValidator import *

SITE_IP = "0.0.0.0"
PORT = 443
app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['POST', 'GET'])
@app.route('/<path:path>')
def proxy(path):
    json_data = request.json

    if validate(json_data):
        return get(f'http://{SITE_IP}:{PORT}/{path}').content  # make request to actual host
    else:
        abort(400, "Invalid json")


def start(site_ip, server_ip, port):
    global SITE_IP, PORT

    SITE_IP = site_ip
    PORT = port

    app.run(host=server_ip, port=port)
