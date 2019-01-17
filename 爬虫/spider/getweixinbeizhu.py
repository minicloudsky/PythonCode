import itchat
from time import sleep
itchat.login()
friends = itchat.get_friends(update=True)[0:]
print(friends)
m = 0
nickname = []
Username= []
charroom = itchat.get_chatrooms()
print(charroom)
for i in friends:
    beizhu = i['RemarkName']
    nickname.append(beizhu)
    message = "hello,%s: " % str(beizhu)
    Username.append(i['UserName'])
    # itchat.send(msg = message,toUserName=i['Username'])
    print('%s 祝福已经发出' %(beizhu))
    # sleep(1.5)
    m = m+1
print(nickname)
print(Username)