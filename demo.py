from __future__ import print_function
from flask import Flask
from flask import request
import json
#env = sys.argv[1]
#port = sys.argv[2]
import simplejson as json
import datetime
#import cachetools
#from cachetools import TTLCache
import urllib
import requests
#from bson.objectid import ObjectId
import sys
#import traceback
#import traceback2 as traceback
import copy
from flask import Flask, url_for


from flask import Flask
app = Flask(__name__)


@app.route("/getLocation")
def get_location(): 
    try:
        print("######### we are getting location!!! 9561120895 #########")
        return "######### we are getting location!!! 9561120895 #########"
    except Exception,err:
        #import traceback
        #exc_info = sys.exc_info()
        #traceback.print_exception(*exc_info)
        print("failed getting location GGG......")
        

@app.route("/hc")
def hc(): 
    try:
        print("######### I am fine now. ##############")
        return "######### I am fine now. ##############"
    except Exception,err:
        #import traceback
        #exc_info = sys.exc_info()
        #traceback.print_exception(*exc_info)
        print("failed health check.........")
        
        

""" Run on port"""
port = ""
if not port:
    port = 5000

app.run(host='0.0.0.0', port=port,debug=True)
# flask depends on this env variable to find the main file
#export FLASK_APP=hello.py

# now we just need to ask flask to run
#flask run


# * Serving Flask app "hello"
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
