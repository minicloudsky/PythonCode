# coding:utf-8
import json
import  requests
import jsonpath

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

request = requests.get(url,headers = headers)

txt = request.text
str = json.loads(txt) #加载json数据
city_list = jsonpath.jsonpath(str,"$..name")\
# dumps禁用ascii编码,默认转化中文为ASCII
array = json.dumps(city_list ,ensure_ascii=False)
with open("lagoucity.json",'w') as f:
    f.write(array)