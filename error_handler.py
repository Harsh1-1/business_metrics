# from flask import jsonify # We may use this module later on, not required here right now though

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    # To return json response of error
    def to_dict(self):
        return_value = dict(self.payload or ())
        return_value["message"] = self.message
        return return_value