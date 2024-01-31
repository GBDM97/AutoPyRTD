data = [(1,2),(3,4)]

def toPage(o):
    global data
    data = o

def returnData():
    global data
    out = list(data)
    print(str(out[0]))
    return str(out[0])