#coding: utf-8
from wxpy import *
bot = Bot(cache_path=True)
# Bot参数:
# cache_path –
# 设置当前会话的缓存路径，并开启缓存功能；为 None (默认) 则不开启缓存功能。
# 开启缓存后可在短时间内避免重复扫码，缓存失效时会重新要求登陆。
# 设为 True 时，使用默认的缓存路径 ‘wxpy.pkl’。
# console_qr –
# 在终端中显示登陆二维码，需要安装 pillow 模块 (pip3 install pillow)。
# 可为整数 (int)，表示二维码单元格的宽度，通常为 2 (当被设为 True 时，也将在内部当作 2)。
# 也可为负数，表示以反色显示二维码，适用于浅底深字的命令行界面。
# 例如: 在大部分 Linux 系统中可设为 True 或 2，而在 macOS Terminal 的默认白底配色中，应设为 -2。
# qr_path – 保存二维码的路径
# qr_callback – 获得二维码后的回调，可以用来定义二维码的处理方式，接收参数: uuid, status, qrcode
# login_callback – 登陆成功后的回调，若不指定，将进行清屏操作，并删除二维码文件
# logout_callback – 登出时的回调
# 机器人自身
myself = bot.self
# 向文件助手发消息
bot.file_helper.send("Hello from wxpy")
# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
bot.enable_puid('wxpy_puid.pkl')
# friend = bot.friends().search("father")[0]
# 获取所有微信好友
friend = bot.friends(update=False)
# 获取群聊
group = bot.groups(update=False)
# 获取所有公众号
mps  = bot.mps(update=False)
# 获取所有聊天对象
chats = bot.chats(update=False)
# 搜索聊天对象
found = bot.friends().search("杨子蘅",sex=MALE,city='开封')
# 确保搜索结果是唯一的，并取出唯一结果
yang = ensure_one(found)
# print(yang)
# 搜索名称包含 'wxpy'，且成员中包含 `杨子蘅` 的群聊对象
# wxpy_groups = bot.groups().search('wxpy', [yang])
# 在刚刚找到的第一个群里搜索
# group = wxpy_groups[0]
# 搜索该群中所有河南的的群友
found = group.search(province='河南')
# 加好友和建群
# add_friend = bot.add_friend(user,verify_content="")
# 添加用户为好友
# 参数:
# user – 用户对象，或 user_name
# verify_content – 验证说明信息
# 关注公众号
# Bot.add_mp(user)[源代码]
# 添加 / 关注 公众号
# 参数:	user – 公众号对象，或 user_name
# Bot.accept_friend(user, verify_content='')[源代码]
# 接受用户为好友
# 参数:
# user – 用户对象或 user_name
# verify_content – 验证说明信息
# 返回:
# 新的好友对象
# 返回类型:
# wxpy.Friend
friend = bot.friends()
friend = friend[4]
# Bot.create_group(users, topic=None)[源代码]
# 创建一个新的群聊
# 参数:
# users – 用户列表 (不含自己，至少 2 位)
# topic – 群名称
# 返回:
# 若建群成功，返回一个新的群聊对象
# 返回类型:
# wxpy.Group
# new_group = bot.create_group(friend,topic="Python交流")

detail = bot.user_details(friend,chunk_size=50)
# 上传文件
file = bot.upload_file("D:\\test.jpg")
# 阻塞进程，知道消息结束消息监听(例如，机器人被logout时候)
join = bot.join()
# 登出
out = bot.logout()