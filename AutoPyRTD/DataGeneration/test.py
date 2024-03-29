data = [
      {
        'code': "PETRB400",
        'strike': "40.01",
        'buyPrice': "0.60",
        'sellPrice': "1.10",
      },
      {
        'code': "PETRB414",
        'strike': "40.26",
        'buyPrice': "0.50",
        'sellPrice': "1.00",
      },
      {
        'code': "PETRB405",
        'strike': "40.51",
        'buyPrice': "0.13",
        'sellPrice': "0.99",
      },
      {
        'code': "PETRB419",
        'strike': "40.76",
        'buyPrice': "0.55",
        'sellPrice': "0.70",
      },
      {
        'code': "PETRB410",
        'strike': "41.01",
        'buyPrice': "0.15",
        'sellPrice': "0.70",
      },
      {
        'code': "PETRB424",
        'strike': "41.26",
        'buyPrice': "0.14",
        'sellPrice': "0.50",
      },
      {
        'code': "PETRB415",
        'strike': "41.51",
        'buyPrice': "0.30",
        'sellPrice': "0.51",
      },
      {
        'code': "PETRB429",
        'strike': "41.76",
        'buyPrice': "0.14",
        'sellPrice': "0.39",
      },
      {
        'code': "PETRB420",
        'strike': "42.01",
        'buyPrice': "0.10",
        'sellPrice': "0.40",
      },
      {
        'code': "PETRB434",
        'strike': "42.26",
        'buyPrice': "0.14",
        'sellPrice': "0.25",
      },
      {
        'code': "PETRB425",
        'strike': "42.51",
        'buyPrice': "0.10",
        'sellPrice': "0.40",
      },
      {
        'code': "PETRB439",
        'strike': "42.76",
        'buyPrice': "0.14",
        'sellPrice': "0.19",
      },
    ]
type = 'CALL'

def getDryOutput(data, type):
  def avPrice(d):
    return (float(d['sellPrice'])+float(d['buyPrice']))/2
  def strikeDiff(c,p):
    return float(c['strike'])-float(p['strike'])
  print([(avPrice(data[i-1])-avPrice(v))/strikeDiff(v,data[i-1]) for i,v in enumerate(data) if i != 0])
     
getDryOutput(data,type)