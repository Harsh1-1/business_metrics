"""
Author : Mani Garg
Updated By: Harsh Suryavanshi
"""

#All Imports 
from utility_class import Utility
from prometheus_class import prometheus
import requests
from logging_class import Logg
import prometheus_client as prom
import time
import json
from flask import Flask, jsonify, redirect, url_for, g
from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from flask_prometheus_metrics import register_metrics
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from error_handler import InvalidUsage

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['checker']=True

@app.before_first_request
def getting_urls():
    gauge_obj_list=[]
    # url_list=[]
    utility = Utility()
    url_data= utility.get_ymldata()
    if url_data=="Invalid json":
        app.config['checker']=False
        # return flask.redirect(flask.url_for("on_Invalid"))
        print("Invalid")
    else:
        for url, path in url_data.items():
            # print(url)
            # output= initialising(url)
            # if type(output) is list:
            print(gauge_obj_list)
            gauge_obj_list+= initialising(url+path)
            # else:
            #     print(flask.url_for(".on_Invalid"))
            app.config["gauge_list"]= gauge_obj_list
            # print(app.config['gauge_list'])
        # print(app.config["gauge_list"])
        for url, path in url_data.items():
            url_list= list()
            url_list.append(url)
            app.config["urls_list"]= url_list

def initialising(url):
    Logg.make_logfile()
    data={}
    # gauge_obj_list1=[]
    try:
        print("hello")
        data=json.loads(requests.get(url).text)
        print("data is:", data)
        gauge_obj_list1 = prometheus.initialise_gauge_obj(data)
        print(gauge_obj_list1)
        # app.config['status_list']=status_list
        # print(len(gauge_obj_list1))
            # if len(gauge_obj_list1)==0:
            #      print(flask.url_for(".on_Invalid"))
            # else:
        return gauge_obj_list1
    except Exception as excp:
        Logg.write_into_file(excp)



def after_some_time():
    if app.config['checker']==False:
        return redirect(url_for("on_Invalid"))
    else:
        for i in app.config['urls_list']:
            try:
                # print("hello")
                # if len(app.config[gauge_list])==0:
                #      print(flask.url_for(".on_Invalid"))
                # else:
                data=json.loads(requests.get(i+"/metrics").text)
                # print(app.config['gauge_list'])
                prometheus.set_gauge_obj(data, app.config['gauge_list'] )
                # print(app.config['gauge_'])
                #print(app.config['gauge_list'])
            except Exception as excp:
                Logg.write_into_file(excp)
@app.route('/')
def home():
    # getting_urls()
    # list_arg=[app.config["urls_list"] , app.config["gauge_list"]]
    if app.config['checker']==False:
        return redirect(url_for("on_Invalid"))
    else:
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=after_some_time, trigger="interval", seconds=3)
        scheduler.start()

        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())
        return("hello")

@app.route('/register')
def registering_metrics():
    app.config['gauge_list']= list()
    # print(app.config['gauge_list'])
    getting_urls()
    return("ayya")

#For handling api errors
@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
