import tkinter
from tkinter import messagebox
from turtle import update
import requests
import os
from bs4 import BeautifulSoup
from tkinter import *
#同步
def sync(ip_address):
    if os.path.exists('address.txt') == False:
        os.mkdir('sync')
    sync_list = []
    page_list = requests.get('http://'+ip_address).text
    #print(page_list)
    soup = BeautifulSoup(page_list, 'html.parser')
    #print(type(soup))
    for i in soup.find_all(name='a'):
        #print(i)
        sync_list.append(i.string)
    for i in range(len(sync_list)):
        print('正在同步:'+sync_list[i])
        file_address = 'http://' + ip_address + '/' + sync_list[i]
        file = requests.get(file_address, stream = True)
        f = open('sync' + '/' +sync_list[i], "wb")
        for chunk in file.iter_content(chunk_size = 1024):
            if chunk:
                f.write(chunk)
    messagebox.showinfo('同步助手v1.0','同步完成,文件同步在sync文件夹中')

#获取文本框输入
def getTextInput():
    TextInput = Entry.get(IP)
    sync(TextInput)

#关于
def about():
    messagebox.showinfo('同步助手v1.0','作者：是鑫焮唉\n作者B站:https://space.bilibili.com/1143915982\n程序版本:v1.0')

#更新公告
def update_Notice():
    messagebox.showinfo('同步助手v1.0','1.修复大文件传输时需要大量的内存\n2.新增"关于"按钮')

#图形初始化阶段
top = Tk()
top.title('同步助手v1.0')
top.resizable(0,0)

#载入文本
text=tkinter.Label(top,text="欢迎使用同步助手",font=('Times', 20))
text.pack()

#载入按钮
quit_button=tkinter.Button(top,text="关闭",command=top.quit)
quit_button.pack(side = 'bottom')
sync_button=tkinter.Button(top,text="同步",command=getTextInput)
sync_button.pack(side = 'right')
about_button=tkinter.Button(top,text="关于",command=about)
about_button.pack(side = 'left')
update_Notice_button=tkinter.Button(top,text="更新内容",command=update_Notice)
update_Notice_button.pack(side = 'bottom')

#创建文本框
IP = Entry(top)
IP.insert(0, "输入IP地址(提示文字)")
IP.pack(side='right')


top.mainloop()
