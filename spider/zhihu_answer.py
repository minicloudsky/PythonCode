import requests
import re
import codecs
from lxml import etree
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
          'cookie':'q_c1=f625095eb0664c8fa22d2c16e29f4235|1506771832000|1506771832000; r_cap_id="NTJhYTJkODQzNDYxNGU1YmFlYjQwNjY4Yjc4M2I0ZjY=|1506771832|92cf9d74e8bc8689b1e4ad8faf6e9311c62eeeb5"; cap_id="ZmJhOTk4Y2Y5NWIyNDExMDg3ZGU2ZTA5NDIyNTcyZDk=|1506771832|47bcd18c624dbcd6df8c23a334416cef3f7e5e21"; d_c0="AAACJBC6dAyPTs36aiC5urxd80qME08pwns=|1506771833"; _zap=b98afb6d-0ed0-4ad9-b348-8080a9f2247f; z_c0=Mi4xY0M5eUFnQUFBQUFBQUFJa0VMcDBEQmNBQUFCaEFsVk5meEQzV1FCd3RXZDJkdERMYldQVG9uVFozMFE2ZS1XLWNn|1506771839|c147c6937eed68f5bc3fe9754d3ae94533f4bafd; __utma=51854390.1679902518.1506773380.1506825303.1506927717.4; __utmz=51854390.1506927717.4.4.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/52281800; __utmv=51854390.100-1|2=registration_date=20160105=1^3=entry_date=20160105=1; _xsrf=d94b3159-498e-4c16-9332-cb4dbf4aa09e'}
def get_url(num,question_id):
    list = []
    for i in range(1,num+1):
        list.append("https://www.zhihu.com/question/"+str(question_id)+"/answers/created?page="+str(i))
    return list

def get_xpath():
    xpath = []
    for i in range(1,21):
        xpath.append('//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div['+str(i)+"]/div/div[2]/div[1]/span/text()")
    #print(xpath)
    return xpath
def get_answer(num,question_id):
    answer = []
    xpath = get_xpath()
    url = get_url(num,question_id)
    #print(url)
    for i in url:
        req = requests.get(i,headers = header)
        # print(req.status_code)
        txt = req.text.encode('utf-8')
        #print(txt)
        for x in xpath:
            selector = etree.HTML(txt)
            content = selector.xpath(x)
            for con in content:
                answer.append(con)
    with codecs.open("zhihu_answer.txt","r+",encoding='utf-8') as f:
        for i in answer:
            f.write(i)
            f.write("\r\n")
            f.write("\r\n")

    for i in answer:
        print(i)
if __name__ == '__main__':
    question_id = "65532647"
    page_num = 20
    get_answer(page_num,question_id)