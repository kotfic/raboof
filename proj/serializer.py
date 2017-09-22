import json

def serialize(obj):
    return json.dumps(obj)

def deserialize(obj):
    jsonObj = json.loads(obj)
    # Transform second argument based on option specified by first agrument
    option = jsonObj[0][0]
    if option == 'reverse':
        jsonObj[0][1] = reverseTransform(jsonObj[0][1])
    elif option == 'capitalize':
        jsonObj[0][1] = capitalizeTransform(jsonObj[0][1])

    return jsonObj

def reverseTransform(str):
    return str[::-1]
def capitalizeTransform(str):
    return str.upper()
