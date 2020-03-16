#All imports
import yaml
from apigen import apigen
import subprocess
import re
import json
import requests
import validators

# One should avoid importing too many libraries in general, since it makes application hard to debug, makes application bulky, reduces transparency and increases chances of vuln because of external modules
# However, it is an internal application and there is no easy cure of lazyness, well in that case we will go for it ¯\_(ツ)_/¯
"""
This Module provides utilities that can be used at multiple places in application
"""

# Constants
YML_CONFIG_PATH = "data.yml"
class Utility:

    def validate_url(self, url):
        if validators.url(url):
            return True
        return False

    #getting the url
    def validation(self):
        keysRegex= re.compile("^[A-Za-z_][A-Za-z0-9_]*$")
        with open(YML_CONFIG_PATH) as f:
            # url_data = yaml.load(f, Loader=yaml.FullLoader)
            url_data = yaml.load(f)
            for url, path in url_data.items():
                data=json.loads(requests.get(url+path).text)
                for keys in data.keys():
                    if keysRegex.match(keys)==False:
                        return False
                for values in data.values():
                    if type(values)!=int and type(values)!=float:
                        return False

    # This function will return url data from yml file, if it is correct, else it will return blank data with error message 
    def get_ymldata(self):
        yml_data_dict = dict()
        yml_data_dict.setdefault("yml_data",None)
        yml_data_dict.setdefault("status",True)
        yml_data_dict.setdefault("message","OK") #Saitama one XD
        with open(YML_CONFIG_PATH) as f:
            try:
                data = yaml.load(f, Loader=yaml.FullLoader)
            except:
                return "Failed to load yml, check your config" # Ideally we should raise this exception and return it via an error handler #TODO start working from here
            check= self.validation()
            if check== False:
                 return "Invalid json"
            else:
                return data


# if __name__ == '__main__':
#     utility.get_url()
