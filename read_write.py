#encoding:utf-8
import threading
import time

def read():
    f = open("1.txt")
    lin = f.read()
    l=len(lin)
    print(l,lin)
    time.sleep(1)

def write():
    ff=open('2.txt','a+') #  新建文件名  a+表示读写
    fff=open('1.txt')
    line = fff.read()   # read 读出来的是整个文件字符串 readline 读出来的是行 readlines读出来的是整个文件的列表 按照行的读取方式
    ff.write(line)
    time.sleep(1)

if __name=__==__'main'__:  #if 在自身运行改文件的时候会生效，但是在import 该py文件时，不会运行以下程序
  t1=threading.Thread(target=read)
  t2=threading.Thread(target=write)
  t1.start()
  t2.start()
