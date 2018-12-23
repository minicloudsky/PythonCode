#导入对应的包
from numpy import *
import itchat
import PIL.Image as Image
from os import listdir

def get_imgs():#完成主要的下载头像的任务
    #使用热登录(已经登录的程序，再一次运行程序不需要扫描验证码)，执行这一步就会有二维码需要扫描登录
    itchat.auto_login(hotReload=True)
    #获取朋友列表，返回字典类型的数据集，获取好友的索引数
    friends = itchat.get_friends(update=True)[0:256]
    #为图片命名的变量
    num = 0
    #遍历好友列表
    for i in friends:
        #获取好友的头像
        img = itchat.get_head_img(userName=i["UserName"])
        #在项目文件的主创建一个user文件用于放头像，并写入对应的图片名，空白的
        fileImage = open( "D://user//" + str(num) + ".jpg",'wb')
        #将获取到的头像文件写到创建的图片文件中
        fileImage.write(img)
        #关闭资源
        fileImage.close()
        num += 1
#制作大的大头像
def get_big_img():
    #获取usr文件夹所有文件的名称
    pics = listdir("D://user")
    numPic = len(pics)
    #创建图片大小
    toImage = Image.new("RGB", (800, 800))
    #用于图片的位置
    x = 0
    y = 0
    #遍历user文件夹的图片
    for i in pics:
        try:
            #依次打开图片
            img = Image.open("D://user//{}".format(i))
        except IOError:
            print("Error: 没有找到文件或读取文件失败",i)
        else:
            #重新设置图片的大小
            img = img.resize((50, 50), Image.ANTIALIAS)
            #将图片粘贴到最后的大图片上，需要注意对应的位置
            toImage.paste(img, (x * 50, y * 50))
            #设置每一行排16个图像
            x += 1
            if x == 16:
                x = 0
                y += 1
    #保存图片为bigPhoto.jpg
    toImage.save("D://user//" +"bigPhoto.jpg")
    #将做好图片发送东自己的手机上
    itchat.send_image("D://user//" +"bigPhoto.jpg", 'filehelper')
#定义执行的主函数
def main():
    get_imgs()
    get_big_img()
#运行
if __name__=="__main__":
    main()