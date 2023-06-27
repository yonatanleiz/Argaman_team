import sys
import json
from ast import literal_eval


def parse(file_name):
    try:
        with open(file_name) as conf_file:
            conf_data = json.load(conf_file)
        python_dict = literal_eval(conf_data["routing"])
        return python_dict
    except Exception as ex:
        print(ex)
