#coding: utf-8
from bs4 import BeautifulSoup
import requests
import random
import codecs
import os
ua = [ 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        ' Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
         'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
        ' Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        ' Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
         'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)']
url = 'http://www.xicidaili.com/nn/{}'
ip_result = []
def get_ip(page):
    ip_result = []
    for i in range(page):
        try:
            r = requests.get(url.format(str(i)),headers = {'User-Agent':random.choice(ua)},proxies={"http://223.241.79.41:8010"},timeout = 20)
            print(r.status_code)
            soup = BeautifulSoup(r.text,'lxml')
            trs = soup.find_all('tr')
            for tr in trs[1:]:
                tds = tr.find_all('td')
                ip = tds[1].text.strip()
                port = tds[2].text.strip()
                ip_add = tds[3].text.strip()
                ip_type = tds[5].text.strip()
                alive_time = tds[8].text.strip()
                if alive_time[-1]=='天':
                    if ip_type=='HTTP':
                        ip_result.append('http://{}:{}'.format(ip,port))
                    elif ip_type=='HTTPS':
                        ip_result.append('https://{}:{}'.format(ip,port))

        except:
            pass
    print(ip_result)
    return ip_result

def validate_ip(ip_result,ip_path):
    if not  os.path.exists(ip_path):
        os.mkdir(ip_path)
    enable_ip = []
    for i in ip_result:
        try:
            r = requests.get('http://ip.chinaz.com/getip.aspx',proxy = i,timeout = 5)
            print(r.status_code)
        except:
            print("ip validate error")
            pass
        else:
            enable_ip.append(i)
    print("{} ip is available".format(len(enable_ip)))
    s = ""
    for i in enable_ip:
        s+=i
        s+='\n'
    try:
        with codecs.open(ip_path+"ip_proxy.txt",'w',encoding='utf-8') as f:
            f.write(s)
    except:
        print("write ip error")


if __name__ == '__main__':
    ip_path = "D:\\ip"
    ip = get_ip(100)
    validate_ip(ip,ip_path)