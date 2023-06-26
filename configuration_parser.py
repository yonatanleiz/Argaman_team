import sys
import json

NUM_ARGS = 2
FILENAME_INDEX = 1

def parse():
    if len(sys.argv) != NUM_ARGS:
        print("invalid argument number")
        exit()
    
    try:
        with open(sys.argv[FILENAME_INDEX]) as conf_file:
            conf_data = json.load(conf_file)
        return conf_data["routing"]
