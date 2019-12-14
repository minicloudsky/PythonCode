import requests
url = 'http://jwgl.ayit.edu.cn/xscj/Stu_MyScore_Drawimg.aspx?x=1&h=2&w=873&xnxq=20170&xn=2017&xq=0&rpt=1&rad=2&zfx=0&xh=201500002964'
headers = {
    'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Cookie':'ASP.NET_SessionId=yge3ov551as2c045lfg5xkrw',
    'Host':'jwgl.ayit.edu.cn',
    'Pragma':'no-cache',
    'Referer':'http://jwgl.ayit.edu.cn/xscj/Stu_MyScore_rpt.aspx',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}

response = requests.get(url,headers=headers)

with open('g.jpg','wb') as f:
    f.write(response.content)