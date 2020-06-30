# Import libraries
import os
import sys
import random
import math
import re
import time
import logging
import argparse
import json
import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4
import requests
from flask import Flask, jsonify, request
from config import ExtractorConfig
# Root directory of the project
ROOT_DIR = os.path.abspath("../")
sys.path.append(ROOT_DIR)  # To find local version of the library
config = ExtractorConfig()
# Logging confg
try:
   logging.basicConfig(level= config.LOGGINGLEVEL,handlers=[
        logging.FileHandler("{0}/{1}.log".format("/logs", "extractionservice-flaskapp")),
        logging.StreamHandler()
    ],
                format="%(asctime)-15s %(levelname)-8s %(message)s")
except: 
   pass
PREFIX_PATH=config.SHARED_DATA_PATH
# Create model object in inference mode.
module = __import__(config.MODEL_MODULE, fromlist=[config.MODEL_CLASS])
my_class = getattr(module,config.MODEL_CLASS)
extractor = my_class()
logging.info("Dynamic loading completed for %s.%s",config.MODEL_MODULE,config.MODEL_CLASS)

def run_extract_content(data):
    # Expecting {filename:'path'}
    logging.info('Loading data: %s with type %s', data, type(data))
    allresults=[]
    for entry in data:
        counter=0
        logging.debug("Processing: %s ",entry['filename'])
        content = extractor.extract(PREFIX_PATH+entry['filename'])
        logging.debug("Managed to extract: %s",content)
        for para in content:
           myresult={'filename':entry['filename'],'id':counter,'content':para.strip()}
           logging.debug("Building entry: %s",myresult)
           counter+=1
        #myresult={'filename':entry['filename'],'id':entry['id'],'section':section,'content':content}
        #myresult={'filename':entry['filename'],'section':section,'content':content}
           #logging.debug(myresult)
           allresults.append(myresult)
    
    return allresults


# Instantiate the Node
app = Flask(__name__)

@app.route('/extract_content', methods=['POST'])
def extract_content_get():
    logging.info("Received extract content request")
    if request.method == 'POST':
        logging.info("Extracting request")
        request_json = request.get_json(force=True)
        if isinstance(request_json,str):
           logging.warn("Somehow json is not received, attempting to convert it %s", request_json)
           request_json=json.loads(request_json)
        logging.info("Sending request to extraction")
        result = run_extract_content(request_json)
        logging.info("Extraction complete, dumping results %s",str(result))
        response_msg = json.dumps(result)
        response = {
           'results': result
        }
        #response=json.dumps(response)
        #print(response)
        return jsonify(response), 200

@app.route('/test', methods=['GET'])
def test_get():
    extractor.extract('test.txt')
    return "ok", 200


if __name__ == '__main__':

    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=9898, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port, debug=True)
