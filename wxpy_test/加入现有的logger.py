import logging
from wxpy import WeChatLoggingHandler
# 这是你现有的 Logger
logger = logging.getLogger(__name__)

# 初始化一个微信 Handler
wechat_handler = WeChatLoggingHandler()
# 加到入现有的 Logger
logger.addHandler(wechat_handler)
logger.warning('你有一条新的告警，请查收。')