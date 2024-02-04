import json

data = []
def toEndpoint(o):
    global data
    data = o

def returnData():
    global data
    return data