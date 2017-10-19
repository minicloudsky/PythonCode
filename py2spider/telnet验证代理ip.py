#coding: utf-8
import telnetlib
try:
    telnetlib.Telnet('175.170.127.58', port='1205', timeout=20)
except:
    print 'connect failed'
else:
    print 'success'
# //*[@id="list"]/table/tbody/tr[1]/td[1]
# //*[@id="list"]/table/tbody/tr[1]/td[2]
# //*[@id="list"]/table/tbody/tr[15]/td[1]
# //*[@id="list"]/table/tbody/tr[15]/td[2]