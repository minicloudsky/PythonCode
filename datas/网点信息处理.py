# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:58:03 2020

@author: Lenovo
"""

import pandas as pd

import requests

import json

from datetime import timedelta, datetime

# %%处理网点
df = pd.read_excel('线下整备底表_crosstab.xlsx', index=False)

df.loc[df['开始网点'].isnull(), '开始网点'] = df[df['开始网点'].isnull()]['结束网点']

# df['网点'] = df[['开始网点', '结束网点']].apply(lambda x: ';'.join(x.dropna()), axis=1)
# df['lag'] = df.sort_values('A').groupby('C')['A'].shift(1)

df = df[(df['调度类型'] == '整备') & (df['处理时长'] > 10) & (df['处理时长'] <= 60)]

df['下一单网点'] = df.sort_values('开始时间').groupby('调度员')['开始网点'].shift(-1)


# %%
def get_dis_tm(startloc, endloc):
    url = 'https://restapi.amap.com/v3/direction/driving?'
    key = '9926d7c4e86c3ac050e8883ad8032091'
    link = '{}origin={}&destination={}&key={}'.format(url, startloc, endloc, key)
    response = requests.get(link)
    dis = ""
    tm = ""
    if response.status_code == 200:
        results = response.json()
        if results['status'] == '1':
            dis += str(float(results['route']['paths'][0]['distance']) * 1.0 / 1000)
            tm += str(float(results['route']['paths'][0]['duration']) / 60)
        else:
            print(link)
    return dis, tm


# %%
startloc = "18.997739, 72.841280"
endloc = "18.880253, 72.945137"
get_dis_tm(startloc, endloc)

"""问题1：这里怎么将startloc、endloc换成df['开始网点']、df['下一单网点']"""

# %%
if tm < df['处理时长']:
    print('异常')
else:
    print('无异常')

"""问题2：这里报错，怎么实现这样的效果"""
# %%
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBAQprXnuq13kMu0sq3RoEprSYXrGt64sE')

now = datetime.now()
directions_result = gmaps.directions("18.997739, 72.841280",
                                     "18.880253, 72.945137",
                                     mode="driving",
                                     avoid="ferries",
                                     departure_time=now
                                     )
print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])

"""问题3：同问题1，怎么直接将经纬度换成df表中的经纬度（这里暂时还没有经纬度，以位置替代）"""
