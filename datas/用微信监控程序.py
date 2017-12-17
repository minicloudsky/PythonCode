from wxpy import get_wechat_logger
from wxpy import *
import requests
# 获得一个专用 Logger
# 当不设置 `receiver` 时，会将日志发送到随后扫码登陆的微信的"文件传输助手"
logger = get_wechat_logger()
# 发送警告
logger.warning('这是一条 WARNING 等级的日志，你收到了吗？')
# 接收捕获的异常
r = requests.get("https://zhihu.com")
try:
    34/0
    # r = requests.get("https://zhihu.com")
except:
    logger.exception(r.text)
