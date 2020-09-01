#docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python your-daemon-or-script.py
from __future__ import print_function
from flask import Flask
from flask import request, render_template
import json
import uuid
import random
#env = sys.argv[1]
#port = sys.argv[2]
from flask import Flask
import simplejson as json
import uuid
import random
import datetime
#import cachetools
#from cachetools import TTLCache
import urllib
import requests
#from bson.objectid import ObjectId
import sys
import traceback
import copy
import uuid
from flask import Flask, url_for


from flask import Flask
app = Flask(__name__)


@app.route("/getLocation")
def get_location(): 
    try:
        print("######### we are getting location!!! #########")
        return "######### we are getting location!!! #########"
    except Exception,err:
        import traceback
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)
        print("failed getting location......")
        

@app.route("/hc")
def hc(): 
    try:
        print("######### I am fine. ##############")
        return "######### I am fine. ##############"
    except Exception,err:
        import traceback
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)
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
