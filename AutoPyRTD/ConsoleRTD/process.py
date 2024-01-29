from AutoPyRTD.ConsoleRTD.output import toConsole

callCodes = ['A','B','C','D','E','F','G','H','I','J','K','L']

def optData(data, dryOrLock):
    options_type = 'CALL' if any(map(lambda l: l == data[0]['code'][-4:-3], callCodes)) else 'PUT'
    toConsole({i['code']: i['sellPrice'] for i in data}) if dryOrLock == 'DRY' else None
    
