import json
import requests

data = {
    "command": "cmds.polyCube",
    "kwargs": {
        "name": "MyCube"
    }
}

# r = requests.post("http://127.0.0.1:6000/command", data=json.dumps(data))
# r = requests.post("http://127.0.0.1:6000/node", data=json.dumps({"name": "group1"}))
r = requests.get("http://127.0.0.1:6000/node")
# r = requests.get("http://127.0.0.1:6000/shutdown")
# r = requests.get("http://127.0.0.1:6000/node")
print r.text
