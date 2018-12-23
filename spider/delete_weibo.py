
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
 
ffbrowser = webdriver.Chrome()
wait = ui.WebDriverWait(ffbrowser,12)
 
def LoginWeibo(username,password):
    try:
    	ffbrowser.get('https://weibo.com/')
        ffbrowser.find_element_by_id('loginname').send_keys(username)
		ffbrowser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(password)
		time.sleep(2)
    except Exception as e:
        print(e)
    finally:
        pass
 
def DeleteWeibo():
    try:
        time.sleep(6)
        elists=ffbrowser.find_elements_by_css_selector(".W_ficon.ficon_arrow_down.S_ficon")
        for e in elists[1:]:
            e.click()
            time.sleep(2)
            ees=ffbrowser.find_elements_by_css_selector(".screen_box>.layer_menu_list>ul>li>a")
            print(ees[0].text)
            ees[0].click()
            time.sleep(1)
            eenter=ffbrowser.find_element_by_css_selector(".W_btn_a>span")
            eenter.click()
            time.sleep(2)
            try:
                time.sleep(1)
                eclose=ffbrowser.find_element_by_css_selector(".W_ficon.ficon_close.S_ficon")
                eclose.click()
                time.sleep(2)
            except:
                pass
 
    except Exception as e:
        print(e)
    finally:
        pass
 
 
if __name__ == '__main__':
    print("开始登录微博")
    LoginWeibo("15716302402","jyw83139200..")
    print("登录成功")
    i=1
    while True:
        print("开始第"+str(i)+"轮删除")
        time.sleep(6)
        DeleteWeibo()
        i+=1