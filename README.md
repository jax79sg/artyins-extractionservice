# Extraction Service For artyins deployment architecture
This is a submodule for the artyins architecture. Please refer to [main module](https://github.com/jax79sg/artyins) for full build details.

[![Build Status](https://travis-ci.com/jax79sg/artyins-extractionservice.svg?branch=master)](https://travis-ci.com/jax79sg/artyins-extractionservice)
[![Container Status](https://quay.io/repository/jax79sg/artyins-extractionservice/status)](https://quay.io/repository/jax79sg/artyins-extractionservice)


Refer to [Trello Task list](https://trello.com/c/mKnW1fgx) for running tasks.

---

## Table of Contents (Optional)

- [Usage](#Usage)
- [Contribution](#Contribution)
- [Virtualenv](#Virtualenv)
- [Tests](#Tests)

---

## Usage
The extraction service can be called by a HTTP POST call. Primarily on http://artyins-extractionservice:9891/extract_content. It expects a json of the following format
```json
[{"filename":"file01.pdf",},{"filename":"file02.pdf"}]
```
After the content is successfully extracted, it will return a json of the following format
```json
{"results":[{"filename":"file01.pdf","id":1,"section":"observation","content":"adfsfswjhrafkf"},{"filename":"file02.pdf","id":2,"section":"observation","content":"kfsdfjsfsjhsd"}]}
```
### config.py
The configuration file will indicate the extractor class to use. For testing purposes, the tika library is used. 
```python
    MODEL_MODULE="extractors.tikextractor"  #Dynamic loading of the required class. There is no need to change codes.
    MODEL_CLASS="TIKExtractor"
    SHARED_DATA_PATH="/shareddata/processing/"
    LOGGINGLEVEL=logging.DEBUG
```
### Contribution
## Abstract Extraction Class
For dynamic loading to function, all implementations of extractors must implement this abstract class.
```python
from abc import ABC, abstractmethod
class ExtractorInterface(ABC):
    """  An abstract base class for report extraction tools """

    @abstractmethod
    def __init__(self):
        raise NotImplementedError()

    @abstractmethod
    def extract(self, fileobject):
        raise NotImplementedError()
```

### An example on how to implement the above Abstract Extraction class
```python
from extractors.extractor import ExtractorInterface
import os
from config import ExtractorConfig
import tika
from tika import parser

class TIKExtractor(ExtractorInterface):
    
    def __init__(self,config=None):
        if config == None:
           config = ExtractorConfig() 
        tika.initVM()

    def extract(self, fileobject):
        parsed = parser.from_file(fileobject)
        return parsed["content"], "unknown"
```
### Customising the logic
In the unlikely evenr that you require to custom the existing logic, you may review `flask_app.py`. It is strongly recommended to talk to Jax on this before you get started. Otherwise, by adding your extraction logic indicated above should suffice.

---

## Virtualenv
```shell
python3 -m venv venv
source venv/bin/activate
pip install --user -r requirements.txt`
```
---

## Tests 
This repository is linked to [Travis CI/CD](https://travis-ci.com/jax79sg/artyins-extractionservice). You are required to write the necessary unit tests and edit `.travis.yml` file if you introduce more extraction classes.

### Web Service Test
```bash
#Start gunicorn wsgi server
gunicorn --bind 0.0.0.0:9891 --daemon --workers 1 wsgi:app
```

### Send test POST request
```python
import requests 

URL = "http://localhost:9898/extract_content"
DATA = [{'filename':'/test.pdf',},{'filename':'/test2.pdf'}]
  
# sending get request and saving the response as response object 
r = requests.post(url = URL, json  = DATA) 
print(r) 
# extracting results in json format 
data = r.json()
print("Data sent:\n{}\n\nData received:\n{}".format(DATA,data))
```

---

