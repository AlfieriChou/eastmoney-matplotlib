import json
import requests


def get_kline_ret(symbol, count=210):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
  }
  url = 'https://push2his.eastmoney.com/api/qt/stock/kline/get'
  params = {
    'secid': symbol,
    'fields1': 'f1,f2,f3,f4,f5,f6',
    'fields2': 'f51,f52,f53,f54,f55',
    'klt': '101',
    'fqt': '1',
    'end': '30000101',
    'lmt': str(count),
  }
  r = requests.get(url, params=params, headers=headers)
  return json.loads(r.text)


def get_kline_list(symbol, count=1000):
  ret = get_kline_ret(symbol, count)
  if ret['data'] and ret['data']['klines']:
    kline_list = []
    for index, kline in enumerate(ret['data']['klines']):
      kline_split_arr = kline.split(',')
      kline_list.append(
        {
          'index': index,
          'date': kline_split_arr[0],
          'open': float(kline_split_arr[1]),
          'close': float(kline_split_arr[2]),
          'high': float(kline_split_arr[3]),
          'low': float(kline_split_arr[4]),
        }
      )
    return kline_list
  return []
