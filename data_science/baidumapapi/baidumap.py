import requests

from baidumapapi.config import *


class BaiduMap:
    base_url = 'http://api.map.baidu.com/routematrix/v2/'
    ak = 'xxx'

    def __init__(self, origin_longitude, origin_latitude,
                 destination_longitude, destination_latitude,
                 tactics=None):
        self.origin_longitude = origin_longitude
        self.origin_latitude = origin_latitude
        self.destination_longitude = destination_longitude
        self.destination_latitude = destination_latitude
        self.tactics = tactics

    # 获取每种出行方式所需时间和距离
    def get_time(self):
        response = {
            ServiceAddress.driving: self.request(ServiceAddress.driving),
            ServiceAddress.riding: self.request(ServiceAddress.riding),
            ServiceAddress.walking: self.request(ServiceAddress.walking),
        }
        return response

    def request(self, service_address):
        request_url = self.base_url \
                      + '{}?output=json&origins={},{}&destinations={},{}&ak={}'.format(service_address,
                                                                                       self.origin_longitude,
                                                                                       self.origin_latitude,
                                                                                       self.destination_longitude,
                                                                                       self.destination_latitude,
                                                                                       self.ak)
        if self.tactics:
            request_url += 'tactics={}'.format(self.tactics)
        response = requests.get(request_url)
        print(request_url)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 0:
                return data['result']
        else:
            return "请求失败"
