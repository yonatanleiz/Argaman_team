from flask import Flask, request, abort
from requests import get
from jsonValidator import *
from filterCommunication import checkSrc

SITE_IP = "0.0.0.0"
PORT = 443
app = Flask(__name__)
NETWORK_CONFIGURATION_FILE = "conf.json"
json_validator = JsonValidator("schemas")


@app.route('/', defaults={'path': ''}, methods=['POST', 'GET'])
@app.route('/<path:path>')
def proxy(path):
    global json_validator
    json_data = request.json

    if not checkSrc(NETWORK_CONFIGURATION_FILE, request.remote_addr):
        abort(401, "Invalid source address")

    if json_validator.validate_json(json_data):
        return get(f'https://{SITE_IP}:{PORT}/{path}').content  # make request to actual host
    else:
        abort(400, "Invalid json")


def start(site_ip, server_ip, port, schemas_path, cert_path, private_key_path):
    global SITE_IP, PORT, json_validator

    SITE_IP = site_ip
    PORT = port

    json_validator = JsonValidator(schemas_path)
    app.run(host=server_ip, port=port, ssl_context=(cert_path, private_key_path))
