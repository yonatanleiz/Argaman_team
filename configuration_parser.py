import sys
import json


# from ast import literal_eval


def parse(file_name):
    try:
        with open(file_name) as conf_file:
            conf_data = json.load(conf_file)

        # TODO: change the ips to real ones
        return conf_data
    except Exception as ex:
        print(ex)
