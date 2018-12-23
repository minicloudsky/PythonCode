import requests
import aiohttp
import re
from lxml import etree
class Anjuke():

    def __init__(self):
        self.header = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'cache-control': 'max-age=0',
            'referer': 'https://anyang.anjuke.com/',
            'upgrade-insecure-requests': ' 1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.all_city = {}
        self.response = requests.get('https://www.anjuke.com/sy-city.html',headers = self.header)
        regex = r'<a href="https://(\w+).anjuke.com">(.+?)</a>'
        city = re.findall(re.compile(regex),self.response.text)
        city = list(set(city))
        print(len(city))
        for citys in city:
            self.all_city[citys[1]] = citys[0]
        # print(self.all_city['洛阳'])
        self.response = requests.get('https://luoyang.anjuke.com/',headers = self.header)
        regex = r'<a class="a_navnew" hidefocus="true" href="(.+?)" _soj="navigation">新 房</a>'
        result = re.findall(re.compile(regex),self.response.text)[0]
        print(result)
if __name__ == '__main__':
    anjuke = Anjuke()
