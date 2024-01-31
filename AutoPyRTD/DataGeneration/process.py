from . import output

callCodes = ['A','B','C','D','E','F','G','H','I','J','K','L']

def getLockOutput(data, type):
    all_lock_combinations = [
        (i['strike'],i['code']+"("+i['strike']+")",ii['code']+"("+ii['strike']+")",
        (float(i['sellPrice'])-float(ii['buyPrice']))/(float(ii['strike'])-float(i['strike']))) 
        for i in data for ii in data if ii['code'] != i['code'] and ii['strike'] >= i['strike']
    ] if type == 'CALL' else [ #output: buy/sell
        (i['strike'],i['code']+"("+i['strike']+")",ii['code']+"("+ii['strike']+")",
        (float(ii['sellPrice'])-float(i['buyPrice']))/(float(ii['strike'])-float(i['strike']))) 
        for i in data for ii in data if ii['code'] != i['code'] and ii['strike'] >= i['strike']
    ]#output: sell/buy
    
    return list(filter(lambda l: l[3] <= 0.25 ,sorted(all_lock_combinations, key=lambda x: x[0],reverse=False if type == 'CALL' else True)))

def optData(data, dryOrLock):
    options_type = 'CALL' if any(map(lambda l: l == data[0]['code'][-4:-3], callCodes)) else 'PUT'
    output.toPage({i['code']: i['sellPrice'] for i in data}) if dryOrLock == 'DRY' else output.toPage(getLockOutput(data, options_type))

    