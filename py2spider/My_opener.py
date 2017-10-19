import urllib2
import requests
http_handler = urllib2.HTTPHandler()
opener = urllib2.build_opener(http_handler)
request = requests.get("http://www.baidu.com")
response = opener.open(request)
print response.read()