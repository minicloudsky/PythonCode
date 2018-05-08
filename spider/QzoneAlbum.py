#!coding:utf-8
from selenium import webdriver
import requests,time,json

login_uin = '3013568147' #登录qq
pwd = 'appijyw231870t;;' #登录密码
album_uin = '935167163' #要读取相册的qq

s = requests.Session()

#实例化出浏览器开始登录
driver = webdriver.Chrome()
driver.set_window_size(1000,600)
driver.get('https://mobile.qzone.qq.com')
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys(login_uin)
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys(pwd)
driver.find_element_by_id('go').click()
#等待浏览器中js计算出qzonetoken
while True:
    qzonetoken = driver.execute_script("return window.shine0callback")
    if qzonetoken:
        break
    time.sleep(0.1)
#读取cookie后关闭浏览器
cookies = driver.get_cookies()
driver.quit()

cookies_ = {}
for cookie in cookies:
    if cookie['name'] == 'p_skey':
        skey = cookie['value']
    #s.cookies.set(cookie['name'], cookie['value'])
    cookies_[cookie['name']] = cookie['value']

#计算gtk
e = 5381
for i in range(len(skey)):
    e = e + (e<<5)+ord(skey[i])
g_tk = str(2147483647 & e)

###################### www.zh30.com ######################

#请求中添加cookie，开始读取相册列表
requests.utils.add_dict_to_cookiejar(s.cookies, cookies_)
url="https://mobile.qzone.qq.com/list?qzonetoken="+qzonetoken+"&g_tk="+g_tk+"&format=json&list_type=album&action=0&res_uin="+album_uin+"&count=50"
r = s.get(url);
data = json.loads(r.text.encode('utf-8'))

for album in data['data']['vFeeds']:
    print ('相册名:'+album['pic']['albumname'].encode('utf-8'))
    print ('相册id:'+album['pic']['albumid'].encode('utf-8'))
    print ('图片数量:' + str(album['pic']['albumnum']))
    print ('开始下载相册图片:')
    #读取当前相册中的图片列表
    url = "https://h5.qzone.qq.com/webapp/json/mqzone_photo/getPhotoList2?qzonetoken="+qzonetoken+"&g_tk="+g_tk+"&uin="+album_uin+"&albumid="+album['pic']['albumid'].encode('utf-8')+"&ps=0"
    r = s.get(url)
    photo_datas = json.loads(r.text.encode('utf-8'))
    for T in photo_datas['data']['photos']:
        for pic in photo_datas['data']['photos'][T]:
            print ('图片名:'+pic['picname'].encode('utf-8')+'，url:'+pic['1']['url'].encode('utf-8'))
    print ("="*10)