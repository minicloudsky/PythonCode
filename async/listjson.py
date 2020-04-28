import re

s = 'window.g_qzonetoken = \(function\()\{ try\{return "(.+?)";\} catch\(e)'
str = """window.g_qzonetoken = (function(){ try{return "a913a685d9156826da939edfb4b721c998936920d59cc2e9baa9c9be456d151e5a8914fa744447f093a5";} catch(e) {var xhr = new XMLHttpRequest();xhr.withCredentials = true;xhr.open('post', '//h5.qzone.qq.com/log/post/error/qzonetoken', true);xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');xhr.send(e);}})();
"""
result = re.findall(re.compile(s), str)
print(result)
