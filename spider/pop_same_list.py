# coding:utf-8
import sys,urllib.request
url = "https://movie.douban.com/subject/26920017/comments?status=P"
wp = urllib.request.urlopen(url)
content =['春风十里，不如你\n', '春风十里，不如你 的豆瓣评分:6.4\n', '春风十里，不如你  6星评价(力荐):14.8%\n', '春风十里，不如你  5星评价(推荐):25.0%\n', '春风十里，不如你  4星评价(还行):33.6%\n', '春风十里，不如你  3星评价(较差):17.3%\n', '春风十里，不如你  2星评价(很差):9.3%\n', '春风十里，不如你 29611人看过\n', '春风十里，不如你 9279人在看\n', '春风十里，不如你 的短评人数:全部 16210 条\n', '春风十里，不如你 电影类型:剧情\n', '(2017)的开播时间:(2017)\n', '集数:\n']
string = ""
for i in content:
    fp = open("web.txt", "w")
    fp.write(i)
    fp.close()
