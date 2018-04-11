s = ""
file = open("D:\\lyric.txt",'r+')
while 1:
    one = file.readline()
    two = file.readline()
    if not one or not two:
        break
    s +="""<span class="comments">{}</span><br/>
                        """.format(one)
    # s+="""<span class="say">{}</span><br>
    #                     <br>""".format(two)
print(s)
