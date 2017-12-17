from wxpy import *
import codecs
bot = Bot(cache_path=True)
bot.enable_puid('wxpy_puid.pkl')
group = bot.groups()
# Bot.register(chats=None, msg_types=None, except_self=True, run_async=True, enabled=True)[源代码]
# 装饰器：用于注册消息配置
# 参数:
# chats – 消息所在的聊天对象：单个或列表形式的多个聊天对象或聊天类型，为空时匹配所有聊天对象
# msg_types – 消息的类型：单个或列表形式的多个消息类型，为空时匹配所有消息类型 (SYSTEM 类消息除外)
# except_self – 排除由自己发送的消息
# run_async – 是否异步执行所配置的函数：可提高响应速度
# enabled – 当前配置的默认开启状态，可事后动态开启或关闭
text = ""
path = "D:\\wechat"
@bot.register(Group,TEXT)
def print_group_msg(msg):
    s = ""
    with codecs.open("E:\\wechat\\temp.txt",'w',encoding='utf-8') as f:
        f.write(msg.text)
    print(msg)
my_friend = bot.friends().search("杨子蘅")[0]
boring_group = bot.groups().search("wxpy_test")[0]
# 打印所有其他信息
@bot.register()
def just_print(msg):
    #打印信息
    print(msg)
    with codecs.open("E:\\wechat\\temp.txt",'w',encoding='utf-8') as f:
        f.write(msg.text)
# 自动回复
@bot.register([my_friend,Group],TEXT)
def auto_reply(msg):
    #如果是群聊，但没有被@，则不回复
    with codecs.open("E:\\wechat\\temp.txt",'w',encoding='utf-8') as f:
        f.write(msg.text)
    if isinstance(msg.chat,Group) and not msg.is_at:
        return
    else:
    #回复消息内容和类型
        return '收到消息: {} ({})'.format(msg.text,msg.type)

@bot.register(boring_group)
def ignore(msg):
    #什么也不做
    return
# 动态开关注册配置
bot.registered
#关闭所有注册配置
# 阻塞线程，并且进入命令行
bot.registered.disable()
# 重新开启just_print函数
bot.registered.enable(just_print)
# 查看当前开启的注册配置
bot.registered.enabled

embed()
