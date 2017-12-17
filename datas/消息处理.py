#coding: utf-8
from wxpy import *
bot = Bot(cache_path=True)
bot.enable_puid('wxpy_puid.pkl')
# 每当机器人接收到消息时，会自动执行以下两个步骤
# 将消息保存到 Bot.messages 中
# 查找消息预先注册的函数，并执行 (若有匹配的函数)
# 消息对象
# 消息对象代表每一条从微信获取到的消息。
# 消息类型可以为以下值
# 文本
TEXT = 'Text'
# 位置
MAP = 'Map'
# 名片
CARD = 'Card'
# 提示
NOTE = 'Note'
# 分享
SHARING = 'Sharing'
# 图片
PICTURE = 'Picture'
# 语音
RECORDING = 'Recording'
# 文件
ATTACHMENT = 'Attachment'
# 视频
VIDEO = 'Video'
# 好友请求
FRIENDS = 'Friends'
# 系统
SYSTEM = 'System'
message = None
company_group = ensure_one(bot.groups().search("wxpy_test"))
# 定位
boss = ensure_one(company_group.search("瞻彼淇奥"))
# 将老板的消息转发到文件传输助手
@bot.register(company_group)
def forward_boss_message(msg):
    message = msg.text
    if msg.member == boss:
        # 把消息转发给文件传输助手
        msg.forward(bot.file_helper, prefix='老板发言')
print(message)
# 阻塞线程
embed()