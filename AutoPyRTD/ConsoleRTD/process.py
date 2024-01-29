from . import output

callCodes = ['A','B','C','D','E','F','G','H','I','J','K','L']

def getLockOutput(data, type):
    all_lock_combinations = [
    (i['strike'],i['code'],ii['code'],
     (float(i['sellPrice'])-float(ii['buyPrice']))/(float(ii['strike'])-float(i['strike']))) 
     for i in data for ii in data if ii['code'] != i['code']
    ] if type == 'CALL' else []
    return all_lock_combinations

def optData(data, dryOrLock):
    options_type = 'CALL' if any(map(lambda l: l == data[0]['code'][-4:-3], callCodes)) else 'PUT'
    output.toConsole({i['code']: i['sellPrice'] for i in data}) if dryOrLock == 'DRY' else output.toConsole(getLockOutput(data, options_type))

    
