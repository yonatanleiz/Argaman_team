import json
import jsonschema
from jsonschema import validate
import os

class json_validator:
    '''
    The class validates a json
    '''

    def __init__(self, schema_dir_path):
        '''
        @brief: receive dir that contains schena files and saves them localy

        @param: The dir path
        '''
        self.schemas = []

        for filename in os.listdir(schema_dir_path):
            filePath = os.path.join(schema_dir_path, filename)

            if os.path.isfile(filePath):
                with open(filePath) as schema:
                    self.schemas.append(json.load(schema))


    def validate_json(self, json_to_validate):
        '''
        @brief: The function receives a json and checks if it valid using the given schemas

        @param: The json to validate

        @return: True if the json is valide, False if not
        '''
        json_to_validate = json_validator.__string_to_json(json_to_validate)
        for schema in self.schemas:
            try:
                validate(instance=json_to_validate, schema=schema)
                return True
            except jsonschema.exceptions.ValidationError as err:
                pass

        return False

    @staticmethod
    def __string_to_json(json_string):
        '''
        @brief: The function recevie string and convert it to json format

        @param: The string to convert

        @return: the json which is created by the given string
        '''
        return json.loads(json_string)

