import re
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
# print(len(content))
# print(result)
# print(result.group())
# print(result.span())
# 泛匹配
result = re.match("^Hello.*Demo$",content)
# print(result)
# print(result.group())
# print(result.span())
# result = re.match('^Hello\s(\d+)\sWorld.*Demo$',content)
# print(result)
# print(result.group(1))
# print(result.span())

# 贪婪模式
# result = re.match('^He.*(\d+).*Demo$',content)
# print(result)
# print(result.group(1))

# .*? 非贪婪模式,尽量匹配少的字符
result = re.match('^He.*?(\d+).*Demo$',content)
print(result)
print(result.group(1))

# content = '''Hello 1234567 World_This
# is a Regex Demo'''
# result = re.match('^He.*?(\d+).*?Demo$',content)
# print(result)

# 转义字符
# content = '123$32'
# result = re.match('123$32',content)
# print(result)

# re.search 扫描字符串返回第一个成功的匹配
content = "Extra strings Hello 1234567 Word_This is a Regex Demo"
result = re.search('Hello.*?(\d+)Demo',re.S)
print(result)