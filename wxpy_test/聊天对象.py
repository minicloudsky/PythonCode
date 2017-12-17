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
# add_friend = friend.add()
# 该聊天对象的昵称 (好友、群员的昵称，或群名称)
nickname = friend.nick_name
# 该聊天对象的友好名称
# 具体为: 从 备注名称、群聊显示名称、昵称 (或群名称)，或微信号中
# 按序选取第一个可用的
name = friend.name
# 以原始格式发送其他类型的消息发送
# friend.send_msg("Hello wxpy")
mp = bot.mps(update=False)
count = 0
friend.send_raw_msg(
    # 名片的原始消息类型
    raw_type=42,
    # 注意 `username` 在这里应为微信 ID，且被发送的名片必须为自己的好友
    raw_content='<msg username="wxpy_bot" nickname="wxpy 机器人"/>'
)
friend.send_raw_msg(
    raw_type = 42,
    raw_content = '<MP: Python中文社区>',
)
# 获取最近的所有群聊
group = bot.groups(update=False)
# print(group)
group = group[0]
# 获取群聊中的成员列表
members = group.members
# 搜索群聊中的成员
result = group.search("王照科")
# 返回群主对象
owner = group.owner
# 判断所属bot是否为群管理员
is_owner = group.is_owner
# 机器人自身
self = group.self
# 更新群聊信息
friends = bot.friends()
sunshine = friends.search("杨子蘅")
# print(sunshine)
group.update_group(members_details=True)
# 从群聊中加入用户
# group.add_members(sunshine)
# yang = group.search("杨子蘅")
# 从群聊中移除用户
# group.remove_members(yang)
# 修改群聊名称
# group.rename_group(name="java")
friend = bot.friends().search("杨子蘅")[0]
group = bot.groups().search("wxpy_test")[0]
# 判断一位用户是否在群众只需用in语句
# if friend in group:
#     print("是的，{} 在 {} 中".format(friend.name,group.name))
# 遍历所有群成员
# for member in group:
#     print(member)
# 查看群成员数量
# print(len(group))
# 若需判断一位群成员是否就是某个好友，使用 == 即可:
member = group.search('杨子蘅')[0]
# if member == friend:
    # print('{} is {}'.format(member,friend))
# 在 Chats 对象中，除了最常用到的 search() 外，还有两个特别的方法，
# stats() 与 stats_text()，可用来统计好友或群成员的性别和地区分布:
# total – 总体数量
# sex – 性别分布
# top_provinces – 省份分布
# top_cities – 城市分布
area = bot.friends().stats_text(total=True,sex=True,top_cities=30,top_provinces=20)
group = bot.groups()
group = group[2]
# 批量发送消息
# for i in range(100):
#     group.send("number: {}".format(i))
# 搜索所有自己在手机上发出的消息
message = bot.messages.search(sender=bot.self)
print(message)
# 多条消息的合集，可用于记录或搜索
# max_history
# 设置最大保存条数，即：仅保存最后的 n 条消息。
# 设置历史消息的最大保存数量为 10000 条
bot.messages.max_history = 10000
# 搜索消息记录
# 参数:
# keywords – 文本关键词
# attributes – 属性键值对
# 返回:
# 所有匹配的消息
# 返回类型:
# wxpy.Messages
# 搜索所有自己发送的，文本中包含 'wxpy' 的消息
bot.messages.search('wxpy', sender=bot.self)
