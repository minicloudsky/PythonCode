import requests
from urllib.parse import urlencode
import json
url = 'https://image.baidu.com/search/acjson?'
headers = {
    'Cookie': 'BDqhfp=1%26%260-10-1undefined%26%260%26%261; BAIDUID=F3EBFCA52FF29E73310B0EF7FE2BC962:FG=1; BIDUPSID=F3EBFCA52FF29E73310B0EF7FE2BC962; PSTM=1557896993; H_PS_PSSID=1458_21089_29135_29237_28518_29099_29138_29134_28833_28584; MCITY=-139%3A; delPer=1; PSINO=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%221%22%5D; cleanHistoryStatus=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}
keyword = '可口可乐'
data = {
    'tn': 'resultjson_com',
    'ipn': 'rj',
    'ct': 201326592,
    'is': '',
    'fp': 'result',
    'queryWord': keyword,
    'cl': 2,
    'lm': -1,
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid': '',
    'st': -1,
    'z': '',
    'ic': 0,
    'hd': '',
    'latest': '',
    'copyright': '',
    'word': 1,
    's': '',
    'se': '',
    'tab': '',
    'width': '',
    'height': '',
    'face': 0,
    'istype': 2,
    'qc': '',
    'nc': 1,
    'fr': '',
    'expermode': '',
    'force': '',
    'pn': 30,
    'rn': 30,
    'gsm': '1e',
    # '1560153126448': ''
}
url = url + urlencode(data)
print(url)
response = requests.get(url, headers=headers).text
datas = json.loads(response)
print(datas['data'])
