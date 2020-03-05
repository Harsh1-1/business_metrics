import yaml
class apigen:
    def generating():
        with open(r'data.yml', 'w') as file:
            dict={}
            for i in range(10):
                s= """import flask
import random
from flask import jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    Dict={}
    Dict['or%s']= random.random(),
    Dict['either%s']=random.random(),
    Dict['neither%s']= random.random(),
    return jsonify(Dict)

app.run(host='0.0.0.0', port=%s)"""%(i,i,i, 7500+i)
                name= "dummy"+str(i)+".py"
                f=open(name, "w")
                f.write(s)
                dict['http://172.16.172.116:' +str(7500+i)]=': /metrics'
                    # data.items().append('http://172.16.172.116:'+str(7500+i))
            documents= yaml.dump(dict,file)
                    # data = yaml.load(f, Loader=yaml.FullLoader)
            # documents= yaml.dump('http://172.16.172.116:'+str(7500+i),file)
