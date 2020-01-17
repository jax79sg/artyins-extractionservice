import requests 

URL = "http://127.0.0.1:9891/test"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
print(r) 
