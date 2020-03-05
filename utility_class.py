import yaml
from apigen import apigen
import subprocess
import re
import json
import requests
# import os
class utility:

    #getting the url
    def validation():
        keysRegex= re.compile("^[A-Za-z_][A-Za-z0-9_]*$")
        with open('data.yml') as f:
            url_data = yaml.load(f, Loader=yaml.FullLoader)
            for url, path in url_data.items():
                data=json.loads(requests.get(url).text)
                for keys in data.keys():
                    if keysRegex.match(keys)==False:
                        return False
                for values in data.values():
                    if type(values)!=int and type(values)!=float:
                        return False

    def get_ymlfile():
        # return "http://172.16.172.104:6000/"
        # apigen.generating()
        # subprocess.call('./bashrun.sh', shell=True)
        with open('data.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            check= utility.validation()
            if check== False:
                 return "Invalid json"
            else:
                return data


# if __name__ == '__main__':
#     utility.get_url()
