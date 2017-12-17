import requests
from wxpy import *
# 初始化机器人
bot = Bot()
# 找到需要接收日志的群 -- `ensure_one()` 用于确保找到的结果是唯一的，避免发错地方
group_receiver = ensure_one(bot.groups().search('wxpy_test'))
# 指定这个群为接收者
logger = get_wechat_logger(group_receiver)
r = requests.get("https://www.baidu.com")
try:
    12/0
except:
    logger.exception(r.status_code)
logger.error('打扰大家了，但这是一条重要的错误日志...')
