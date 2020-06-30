import requests
import json
pload = json.dumps([{"filename":"test2.pdf",}])
r = requests.post("http://127.0.0.1:9891/extract_content",data = pload)
print(json.dumps(json.loads(r.text),indent=4))
