from flask import Flask, request, abort
from requests import get
from jsonValidator import *
from filterCommunication import checkSrc

SITE_IP = "0.0.0.0"
PORT = 443
app = Flask(__name__)
NETWORK_CONFIGURATION_FILE = "conf.json"

@app.route('/', defaults={'path': ''}, methods=['POST', 'GET'])
@app.route('/<path:path>')
def proxy(path):
    json_data = request.json

    if not checkSrc(NETWORK_CONFIGURATION_FILE, request.remote_addr):
        abort(401, "Invalid source address")

    if validate(json_data):
        return get(f'http://{SITE_IP}:{PORT}/{patht}').content  # make request to actual host
    else:
        abort(400, "Invalid json")


def start(site_ip, server_ip, port):
    global SITE_IP, PORT

    SITE_IP = site_ip
    PORT = port

    app.run(host=server_ip, port=port)
