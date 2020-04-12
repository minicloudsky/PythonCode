import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from redis import Redis, RedisError
import re
games_key = "games_v1"


def get_redis():
    redis = Redis(host='39.105.154.2', port=6379, password='Redis')
    if redis.ping():
        return redis
    else:
        return RedisError("connection error")


def get_page():
    redis = get_redis()
    if redis.get(games_key):
        html = redis.get(games_key)
    else:
        chrome = webdriver.Chrome()
        chrome.get('https://www.3839.com/top/hot.html')
        chrome.set_window_size(1400, 900)
        chrome.find_element_by_tag_name('body').send_keys(Keys.END)
        for i in range(6):
            chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
        html = chrome.page_source
        redis.set(games_key, html)
    regex = """<li style="display:" .*?<a href="//www.3839.com/a/(.+?).htm"><img .*? src="(.+?)">.+?class="name"><a href="//www.3839.com/a/117126.htm">光明记忆 (测试服)</a></em>
<p class="auth">(.+?)</p>.*?
<span class="score">8.0 分</span>
</div>
</div>
<p class="desc">()</p>
<div class="tags">
<div class="taglist">
<span><a href="//www.3839.com/fenlei/cat_hot_5.html">射击</a></span>
<span><a href="//www.3839.com/fenlei/cat_hot_75.html">冒险</a></span>
<span><a href="//www.3839.com/fenlei/cat_hot_107.html">Steam 移植</a></span>
</div>
<a href="//www.3839.com/a/117126.htm" class="state blue">试玩</a></div>
</div>
<div class="gamePho imgWidth">
<ul>
<li><a href="//fs.img4399.com/sykb~sykb/20191001/16041084808?800x480" onclick="return false;" data-lightbox="screenshots4"><img alt="光明记忆(测试服)截图" src="//fs.img4399.com/sykb~sykb/20191001/16041084808?800x480"></a></li>
</ul>
</div>
</li>"""
if __name__ == '__main__':
    get_page()
