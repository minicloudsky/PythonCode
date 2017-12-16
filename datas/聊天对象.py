#coding: utf-8
from wxpy import *
bot = Bot(cache_path=True)
bot.enable_puid('wxpy_puid.pkl')
my_friend = bot.friends().search("陈金光")
friend = my_friend[0]
# friend.send("Hello,World!")
# friend.send_image("D:\\name.jpg")
# friend.send_video("D:\\video.mp4")
# send file
# friend.send_file("D:\\file.rar")
# print(friend.nickname())
# 获取头像，save_path为保存路径
friend.get_avatar(save_path="D:\\chen.jpg")
# 设置或修改好友备注名称
friend.set_remark_name(remark_name="chenjinguang")
# 性别，MALE = 1,FEMALE  = 2
sex = friend.sex
province = friend.province
signature = friend.signature
is_friend = friend.is_friend
# 添加当前用户为好友
add_friend = friend.add()