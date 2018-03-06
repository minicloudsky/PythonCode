import socket
from urllib import request,error
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.html')
# except error.URLError as e:
#     print(e.reason)
#     if isinstance(e.reason,socket.timeout):
#         print("TIME OUT")
# else:
#     print("Request Successfully")

try:
    response = request.urlopen('http://cuiqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason)

else:
    print("Request Successfully")