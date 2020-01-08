[![Classifier Service](https://github.com/jax79sg/artyins-extractionservice/raw/master/images/SoftwareArchitectureExtractionService.jpg)]()

# Classifier Service For artyins deployment architecture
This is a submodule for the artyins architecture. Please refer to [main module](https://github.com/jax79sg/artyins) for full build details.

[![Build Status](https://travis-ci.com/jax79sg/artyins-extractionservice.svg?branch=master)](https://travis-ci.com/jax79sg/artyins-extractionservice)

Refer to [Trello Task list](https://trello.com/c/mKnW1fgx) for running tasks.

---

## Table of Contents (Optional)

- [Usage](#Usage)
- [Virtualenv](#Virtualenv)
- [Tests](#Tests)

---

## Usage

### config.py
```python
```

### Abstract Extraction Class
```python
```

### An example on how to implement the Abstract Extraction class
```python
```

### Adding your extraction into Web Service
You will need to add your extraction function into the Web Service (flask_app.py). Here is an example, you may simply add your functions.
```python
```
---

## Virtualenv
```shell
python3 -m venv venv
source venv/bin/activate
pip install --user -r requirements.txt`
```
---

## Tests 
This repository is linked to [Travis CI/CD](https://travis-ci.com/jax79sg/artyins-extractionservice). You are required to write the necessary unit tests if you introduce more extraction classes.
### Unit Tests
```python
```

### Web Service Test
```
#Start gunicorn wsgi server
gunicorn --bind 0.0.0.0:9898 --daemon --workers 1 wsgi:app
```
Send test POST request
```python
```

---

