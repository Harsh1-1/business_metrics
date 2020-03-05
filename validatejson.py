from schema import Schema
# from dummy0 import dummy
import json
import requests
class validating:
    def validate(data):

        schema= Schema({
          "type": "object",
          "propertyNames":{
           "pattern" : "^[A-Za-z_][A-Za-z0-9_]*$",
           # for keys in dict.keys():
           "keys" : { "type" : "string" },
           # for values in dict.values():
           "values" : { "type" : "integer" }
           }
        })
        validated= schema.validate(data)
        print(validated)

if __name__ == '__main__':
    data=json.loads(requests.get('http://0.0.0.0:7544/').text)
    validating.validate(data)
