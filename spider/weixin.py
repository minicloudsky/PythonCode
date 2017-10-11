# coding: utf-8
import itchat
from pandas import DataFrame
itchat.login()
friend = itchat.get_friends(update=True)[0:]
print(friend)
male = female = other = 0
for i in friend[1:]:
    sex = i["Sex"]
    if sex ==1:
        male +=1
    elif sex ==2:
        female +=1
    else:
        other +=1
total = len(friend[1:])
print("男性好友: %.2f%%" %(float(male)/total*100)+"\n"+
      "女性好友: %.2f%%" %(float(female)/total*100)+"\n"+"不明性别好友: %.2f%%" %(float(other)/total*100))

#定义一个函数，用来爬取各个变量
def get_var(var):
    variable = []
    for i in friend:
        value = i[var]
        variable.append(value)
    return variable
#调用函数得到各变量，并把数据存到csv文件中，保存到桌面
NickName = get_var("NickName")
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')
data = {'NickName': NickName, 'Sex': Sex, 'Province': Province,
        'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('data.csv', index=True)