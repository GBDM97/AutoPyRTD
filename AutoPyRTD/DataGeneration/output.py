data = []
from pathlib import Path
import os

def toPage(o):
    global data
    data = o

def returnData():
    global data
    out = list(data)
    return str(out) if data else "LOADING DATA ..."