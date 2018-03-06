import requests
from lxml.html import etree
from bs4 import BeautifulSoup
header = {
    'Host':'m.lagou.com',
    'Referer':'https://m.lagou.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4'
}

start_url = 'https://m.lagou.com/jobs/3472437.html'
response = requests.get(start_url,headers = header)
job_name = etree.HTML(response.text).xpath('//*[@id="content"]/div[1]/h2/text()')
job_type = etree.HTML(response.text).xpath('//*[@id="content"]/div[2]/div[1]/span[3]/span/text()')
experience = etree.HTML(response.text).xpath('//*[@id="content"]/div[2]/div[1]/span[4]/span/text()')
education = etree.HTML(response.text).xpath('//*[@id="content"]/div[2]/div[1]/span[5]/span/text()')
job_attract = etree.HTML(response.text).xpath('//*[@id="content"]/div[2]/div[2]/text()')
company = etree.HTML(response.text).xpath('//*[@id="content"]/div[3]/div/div/h2/text()')
company_info = etree.HTML(response.text).xpath('//*[@id="content"]/div[3]/div/div/p/text()')
soup = BeautifulSoup(response.text,'lxml')
job_describe = soup.find_all('div',class_='content')[0].text.strip()
print(job_describe)
print(job_type)
