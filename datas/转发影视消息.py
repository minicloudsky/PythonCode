#coding: utf-8
from wxpy import *
import os
import codecs
import time
bot = Bot(cache_path=True)
bot.enable_puid('wxpy_puid.pkl')
our_group = bot.search("wxpy_test")[0]
movie_group = bot.search("影视资源群")[0]
admin = ensure_one(movie_group.members.search("小可"))
movie_list = ""
path = "E://wechat"
if not os.path.exists(path):
    os.mkdir(path)
# 将群管理发的电影资源转发
@bot.register(movie_group)
def froward_movie_message(msg):
    print(msg.text)
    with codecs.open(path+"\\movie.txt", 'a+', encoding='utf-8') as f:
        f.write(msg.text)
    if msg.member == admin:
        msg.forward(our_group, prefix="影视资源")
# 阻塞线程
embed()

