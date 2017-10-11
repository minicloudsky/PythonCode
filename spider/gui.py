import tkinter
import os
root = tkinter.Tk()
label = tkinter.Label(root,text="                               ").grid(row=0,column=0)
label2 = tkinter.Label(root,text="Pexels 图片网站AJAX 图片爬虫",font = 'STXingkai -25 bold', fg = "#CDC9C9").grid(row=0,column=1)
label3 = tkinter.Label(root,text="                              ").grid(row=1,column=0)
num = tkinter.Text(root,height=5,width=20).grid(row=1,column=1)
label4 = tkinter.Label(root,text="                              ").grid(row=2,column=0)
btn = tkinter.Button(root,text="启动爬虫").grid(row=2,column=1,ipadx="4p", ipady="4p")
root.mainloop()