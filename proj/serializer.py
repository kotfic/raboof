import json

def serialize(obj):
    return json.dumps(obj)

def deserialize(obj):
    jsonObj = json.loads(obj)
    jsonObj[0][0] = strTransform(jsonObj[0][0])
    return jsonObj

def strTransform(str):
    return str[::-1]
