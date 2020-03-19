import json

class JsonDataUtil():

    def __init__(self,value_string):
        self.json_data = json.loads(value_string)


    def retain_fields(self,fields):
        self.new_json_data = {}
        for field in fields:
            self.new_json_data[field]=self.json_data[field]

        self.json_data = self.new_json_data

    def get_value(self,field):
        return self.json_data[field]

    def add_metadata(self,key,value):
        self.json_data[key]=json.loads(value)


    def get_json(self):
        return json.dumps(self.json_data)