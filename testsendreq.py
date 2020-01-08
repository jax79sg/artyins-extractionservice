import requests 

URL = "http://localhost:9898/extract_content"
DATA = [{'filename':'/test.pdf',},{'filename':'/test2.pdf'}]
  
# sending get request and saving the response as response object 
r = requests.post(url = URL, json  = DATA) 
print(r) 
# extracting results in json format 
data = r.json()
print("Data sent:\n{}\n\nData received:\n{}".format(DATA,data))
