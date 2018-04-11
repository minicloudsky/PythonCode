list = ["https:123.jpg","http://df.jpg","&lt"]
for i in list:
     if i[:4] != "http":
            list.remove(i)
print(list)
